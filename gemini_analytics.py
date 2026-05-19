"""
Gemini Analytics Module for Sclera Academic
Provides AI-driven insights for at-risk prediction, readiness scoring, and study pattern clustering
"""
import os
import json
import time
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict
import logging

# Import existing modules
from firebase_config import db
from firebase_admin import firestore
from utils.logger import logger
from utils.cache import cached, CacheManager
from templates.academic_data import get_syllabus

# Enhanced rate limiter to prevent too many concurrent API calls
class RateLimiter:
    def __init__(self, max_calls_per_minute: int = 3, max_calls_per_hour: int = 50):
        self.max_calls_per_minute = max_calls_per_minute
        self.max_calls_per_hour = max_calls_per_hour
        self.calls_minute = []  # Track calls in last minute
        self.calls_hour = []  # Track calls in last hour
        self.lock = threading.Lock()
        self.quota_cooldown_until = 0  # Timestamp until which we're in cooldown
        self.quota_hit_count = 0  # Track how many times we've hit quota
    
    def wait_if_needed(self, model_name: str = None):
        """Wait if rate limit is reached or if in quota cooldown
        
        Args:
            model_name: Optional model name for per-model tracking
        """
        with self.lock:
            now = time.time()
            
            # Check if we're in quota cooldown
            if now < self.quota_cooldown_until:
                wait_time = self.quota_cooldown_until - now
                logger.warning(f"In quota cooldown, waiting {wait_time:.1f}s before retrying")
                time.sleep(wait_time)
                now = time.time()
            
            # Remove calls older than 1 minute
            self.calls_minute = [call_time for call_time in self.calls_minute if now - call_time < 60]
            
            # Remove calls older than 1 hour
            self.calls_hour = [call_time for call_time in self.calls_hour if now - call_time < 3600]
            
            # Check minute limit
            if len(self.calls_minute) >= self.max_calls_per_minute:
                # Calculate how long to wait
                oldest_call = min(self.calls_minute)
                wait_time = 60 - (now - oldest_call)
                if wait_time > 0:
                    logger.info(f"Minute rate limit reached ({self.max_calls_per_minute}/min), waiting {wait_time:.1f}s")
                    time.sleep(wait_time)
                    now = time.time()
                    # Refresh calls after waiting
                    self.calls_minute = [call_time for call_time in self.calls_minute if now - call_time < 60]
            
            # Check hour limit
            if len(self.calls_hour) >= self.max_calls_per_hour:
                # Calculate how long to wait
                oldest_call = min(self.calls_hour)
                wait_time = 3600 - (now - oldest_call)
                if wait_time > 0:
                    logger.warning(f"Hour rate limit reached ({self.max_calls_per_hour}/hour), waiting {wait_time:.1f}s")
                    time.sleep(wait_time)
                    now = time.time()
                    # Refresh calls after waiting
                    self.calls_hour = [call_time for call_time in self.calls_hour if now - call_time < 3600]
            
            # Record this call
            self.calls_minute.append(now)
            self.calls_hour.append(now)
            
            if model_name:
                logger.debug(f"Rate limiter: Call allowed for {model_name} (minute: {len(self.calls_minute)}/{self.max_calls_per_minute}, hour: {len(self.calls_hour)}/{self.max_calls_per_hour})")
    
    def trigger_quota_cooldown(self, duration_seconds: int = 300):
        """Trigger a cooldown period after hitting quota
        
        Args:
            duration_seconds: How long to wait before allowing calls again
        """
        with self.lock:
            self.quota_cooldown_until = time.time() + duration_seconds
            self.quota_hit_count += 1
            logger.warning(f"Quota cooldown triggered for {duration_seconds}s (hit count: {self.quota_hit_count})")
            
            # Increase cooldown duration with repeated quota hits
            if self.quota_hit_count > 1:
                # Exponential backoff: 5min, 10min, 20min, 40min, max 1 hour
                extended_duration = min(3600, 300 * (2 ** (self.quota_hit_count - 1)))
                self.quota_cooldown_until = time.time() + extended_duration
                logger.warning(f"Extended quota cooldown to {extended_duration}s due to repeated quota hits")
    
    def reset_cooldown(self):
        """Reset the quota cooldown (call after successful API call)"""
        with self.lock:
            if self.quota_cooldown_until > time.time():
                logger.info("Quota cooldown reset after successful call")
            self.quota_cooldown_until = 0
    
    def get_stats(self):
        """Get current rate limiter statistics"""
        with self.lock:
            now = time.time()
            return {
                'calls_per_minute': len([t for t in self.calls_minute if now - t < 60]),
                'calls_per_hour': len([t for t in self.calls_hour if now - t < 3600]),
                'quota_hit_count': self.quota_hit_count,
                'in_cooldown': now < self.quota_cooldown_until,
                'cooldown_remaining': max(0, self.quota_cooldown_until - now)
            }

# Circuit breaker to prevent repeated failures
class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 300):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN
        self.lock = threading.Lock()
    
    def call(self, func, *args, **kwargs):
        with self.lock:
            if self.state == 'OPEN':
                if time.time() - self.last_failure_time > self.recovery_timeout:
                    self.state = 'HALF_OPEN'
                    logger.info("Circuit breaker entering HALF_OPEN state")
                else:
                    raise Exception("Circuit breaker is OPEN - API calls disabled")
            
            try:
                result = func(*args, **kwargs)
                # Success - reset failure count and close circuit
                self.failure_count = 0
                if self.state == 'HALF_OPEN':
                    self.state = 'CLOSED'
                    logger.info("Circuit breaker CLOSED - API calls restored")
                return result
            except Exception as e:
                self.failure_count += 1
                self.last_failure_time = time.time()
                
                if self.failure_count >= self.failure_threshold:
                    self.state = 'OPEN'
                    logger.warning(f"Circuit breaker OPENED after {self.failure_count} failures")
                
                raise e

# Global rate limiter and circuit breaker
# Reduced to 3 calls/minute for free tier compatibility
rate_limiter = RateLimiter(max_calls_per_minute=3, max_calls_per_hour=50)  # Very conservative for free tier
circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=300)  # 5 min recovery


class GeminiAnalytics:
    """Main class for Gemini-powered analytics"""
    
    def __init__(self):
        """Initialize with existing AI assistant"""
        try:
            from ai_assistant import get_ai_assistant
            self.ai_assistant = get_ai_assistant()
            self.ai_available = self.ai_assistant.ai_available if self.ai_assistant else False
            
            # Initialize model management for dynamic switching
            self.exhausted_models = set()
            self.available_models = []
            self.current_model_index = 0
            
            if self.ai_available and hasattr(self.ai_assistant, 'available_models'):
                self.available_models = self.ai_assistant.available_models.copy()
                logger.info(f"Initialized with {len(self.available_models)} available models")
        except Exception as e:
            logger.error(f"Failed to initialize AI assistant: {str(e)}")
            self.ai_available = False
            self.exhausted_models = set()
            self.available_models = []
            self.current_model_index = 0
    
    def _get_working_model(self):
        """Get a working model, switching to next available if current is exhausted"""
        if not self.ai_available or not self.available_models:
            return None
        
        # Try to find a non-exhausted model
        for i in range(len(self.available_models)):
            model_name = self.available_models[self.current_model_index]
            
            if model_name not in self.exhausted_models:
                try:
                    # Try to create a new model instance
                    import google.generativeai as genai
                    model = genai.GenerativeModel(model_name=model_name)
                    logger.info(f"Using model: {model_name}")
                    return model
                except Exception as e:
                    logger.warning(f"Failed to create model {model_name}: {e}")
                    self._mark_model_exhausted()
                    continue
            else:
                # Move to next model if current is exhausted
                self.current_model_index = (self.current_model_index + 1) % len(self.available_models)
        
        # All models exhausted, reset after a delay
        logger.warning("All models exhausted, resetting exhausted list after delay")
        self.exhausted_models.clear()
        self.current_model_index = 0
        
        # Try one more time after reset
        if self.available_models:
            model_name = self.available_models[0]
            try:
                import google.generativeai as genai
                model = genai.GenerativeModel(model_name=model_name)
                logger.info(f"Reset complete, using model: {model_name}")
                return model
            except Exception as e:
                logger.error(f"Failed to create model after reset: {e}")
        
        return None
    
    def _mark_model_exhausted(self):
        """Mark current model as exhausted and move to next"""
        if self.available_models and self.current_model_index < len(self.available_models):
            exhausted_model = self.available_models[self.current_model_index]
            self.exhausted_models.add(exhausted_model)
            logger.info(f"Marked model as exhausted: {exhausted_model}")
            
            # Move to next model
            self.current_model_index = (self.current_model_index + 1) % len(self.available_models)
            next_model = self.available_models[self.current_model_index]
            logger.info(f"Switching to next model: {next_model}")
    
    def get_model_status(self):
        """Get current model status for debugging"""
        return {
            'available_models': self.available_models,
            'exhausted_models': list(self.exhausted_models),
            'current_model_index': self.current_model_index,
            'current_model': self.available_models[self.current_model_index] if self.available_models and self.current_model_index < len(self.available_models) else None
        }
    
    def build_student_features(self, uid: str) -> Dict[str, Any]:
        """
        Build comprehensive feature dictionary for a student
        Includes login frequency, study sessions, chapter completion, exam trends, heatmap patterns
        """
        try:
            # Get user document
            user_doc = db.collection('users').document(uid).get()
            if not user_doc.exists:
                return {}
            
            user_data = user_doc.to_dict()
            # Debug: Log what data we're extracting
            study_sessions = self._get_study_session_features(uid)
            chapter_completion = self._get_chapter_completion_features(user_data)
            exam_trends = self._get_exam_trend_features(user_data)
            
            logger.info(f"📊 STUDENT FEATURES for {user_data.get('name', 'Unknown')} ({uid[:8]}...):")
            logger.info(f"  📚 Chapter Completion: {chapter_completion.get('completed_chapters', 0)}/{chapter_completion.get('total_chapters', 0)} ({chapter_completion.get('overall_completion', 0)}%)")
            logger.info(f"  ⏱️  Study Sessions: {study_sessions.get('session_count_30d', 0)} sessions, {study_sessions.get('total_duration_30d', 0)} total minutes")
            logger.info(f"  📈 Exam Trends: {len(exam_trends.get('recent_scores', []))} recent exams")
            
            features = {
                'uid': uid,
                'name': user_data.get('name', 'Student'),
                'purpose': user_data.get('purpose', ''),
                'login_frequency': self._get_login_frequency(user_data),
                'study_sessions': study_sessions,
                'chapter_completion': chapter_completion,
                'exam_trends': exam_trends,
                'heatmap_patterns': self._get_heatmap_patterns(uid),
                'quiz_tests': self._get_quiz_test_features(uid),
                'topic_mastery': self._get_topic_mastery_features(uid)
            }
            
            return features
            
        except Exception as e:
            logger.error(f"Error building features for {uid}: {str(e)}")
            return {}
    
    def _get_login_frequency(self, user_data: Dict) -> Dict[str, Any]:
        """Calculate login frequency metrics"""
        last_login = user_data.get('last_login_date')
        streak = user_data.get('login_streak', 0)
        
        # Calculate days since last login
        days_since_login = 0
        if last_login:
            try:
                last_date = datetime.fromisoformat(last_login)
                days_since_login = (datetime.utcnow() - last_date).days
            except:
                pass
        
        return {
            'last_login_date': last_login,
            'days_since_login': days_since_login,
            'login_streak': streak,
            'recent_activity': days_since_login <= 7
        }
    
    def _get_study_session_features(self, uid: str) -> Dict[str, Any]:
        """Analyze study session patterns"""
        try:
            # Get last 30 days of sessions
            thirty_days_ago = (datetime.utcnow() - timedelta(days=30)).isoformat()
            sessions_ref = db.collection('users').document(uid).collection('study_sessions').where('start_time', '>=', thirty_days_ago).stream()
            
            sessions = []
            total_duration = 0
            
            for session_doc in sessions_ref:
                session_data = session_doc.to_dict()
                sessions.append(session_data)
                total_duration += session_data.get('duration', 0)
            
            if not sessions:
                return {
                    'session_count_30d': 0,
                    'avg_duration': 0,
                    'total_duration_30d': 0,
                    'consistency_score': 0
                }
            
            # Calculate metrics
            avg_duration = total_duration / len(sessions)
            
            # Consistency: sessions per week
            sessions_by_week = defaultdict(int)
            for session in sessions:
                try:
                    session_date = datetime.fromisoformat(session['start_time'])
                    week_num = session_date.isocalendar()[1]
                    sessions_by_week[week_num] += 1
                except:
                    pass
            
            consistency_score = 0
            if sessions_by_week:
                avg_sessions_per_week = sum(sessions_by_week.values()) / len(sessions_by_week)
                consistency_score = min(100, avg_sessions_per_week * 20)  # Scale to 0-100
            
            return {
                'session_count_30d': len(sessions),
                'avg_duration': round(avg_duration, 2),
                'total_duration_30d': total_duration,
                'consistency_score': round(consistency_score, 1)
            }
            
        except Exception as e:
            logger.error(f"Error getting study session features for {uid}: {str(e)}")
            return {'session_count_30d': 0, 'avg_duration': 0, 'total_duration_30d': 0, 'consistency_score': 0}
    
    def _get_chapter_completion_features(self, user_data: Dict) -> Dict[str, Any]:
        """Analyze chapter completion by subject"""
        try:
            chapters_completed = user_data.get('chapters_completed', {})
            
            if not chapters_completed:
                return {'overall_completion': 0, 'by_subject': {}, 'total_chapters': 0, 'completed_chapters': 0}
            
            # Debug: Log what we found
            logger.info(f"    🔍 Found chapters_completed: {list(chapters_completed.keys())}")
            
            # Get syllabus for total chapter counts
            total_by_subject = {}
            
            # Try to get syllabus from class data first
            class_ids = user_data.get('class_ids', [])
            if class_ids:
                # Get syllabus from the first class (simplified)
                try:
                    from firebase_config import db
                    class_doc = db.collection('classes').document(class_ids[0]).get()
                    if class_doc.exists:
                        class_data = class_doc.to_dict()
                        board = class_data.get('board', 'CBSE')
                        grade = class_data.get('grade', '10')
                        purpose = class_data.get('purpose', 'highschool')
                        
                        logger.info(f"    📚 Getting syllabus for class: {board} {grade} ({purpose})")
                        
                        if purpose in ['highschool', 'school']:
                            syllabus = get_syllabus('school', board, grade)
                        else:
                            # Handle JEE/NEET case
                            if 'JEE' in str(board).upper():
                                syllabus = get_syllabus('exam', 'JEE')
                            elif 'NEET' in str(board).upper():
                                syllabus = get_syllabus('exam', 'NEET')
                            else:
                                syllabus = get_syllabus('exam', board)
                        
                        logger.info(f"    📚 Syllabus retrieved with {len(syllabus)} subjects")
                        
                        for subject, data in syllabus.items():
                            total_by_subject[subject] = len(data.get('chapters', {}))
                except Exception as e:
                    logger.warning(f"    ⚠️  Could not get class syllabus: {e}")
                    # Fallback to CBSE 10
                    syllabus = get_syllabus('school', 'CBSE', '10')
                    for subject, data in syllabus.items():
                        total_by_subject[subject] = len(data.get('chapters', {}))
            
            # Fallback to direct user data if no class info
            elif user_data.get('purpose') == 'school' and user_data.get('school'):
                school = user_data['school']
                syllabus = get_syllabus('school', school.get('board'), school.get('grade'), 
                                     subject_combination=school.get('subject_combination'))
                for subject, data in syllabus.items():
                    total_by_subject[subject] = len(data.get('chapters', {}))
            elif user_data.get('purpose') == 'exam_prep' and user_data.get('exam'):
                syllabus = get_syllabus('exam', user_data['exam'].get('type'))
                for subject, data in syllabus.items():
                    total_by_subject[subject] = len(data.get('chapters', {}))
            else:
                # Default fallback to CBSE 10
                syllabus = get_syllabus('school', 'CBSE', '10')
                for subject, data in syllabus.items():
                    total_by_subject[subject] = len(data.get('chapters', {}))
            
            logger.info(f"    📖 Total chapters by subject: {total_by_subject}")
            
            # Calculate completion rates
            by_subject = {}
            total_chapters = 0
            completed_chapters = 0
            
            for subject, completed_chapters_dict in chapters_completed.items():
                total_chapters_subject = total_by_subject.get(subject, 0)
                completed_count = sum(1 for completed in completed_chapters_dict.values() if completed)
                
                if total_chapters_subject > 0:
                    completion_rate = (completed_count / total_chapters_subject) * 100
                    by_subject[subject] = round(completion_rate, 1)
                    total_chapters += total_chapters_subject
                    completed_chapters += completed_count
            
            overall_completion = (completed_chapters / total_chapters * 100) if total_chapters > 0 else 0
            
            return {
                'overall_completion': round(overall_completion, 1),
                'by_subject': by_subject,
                'total_chapters': total_chapters,
                'completed_chapters': completed_chapters
            }
            
        except Exception as e:
            logger.error(f"Error getting chapter completion features: {str(e)}")
            return {'overall_completion': 0, 'by_subject': {}, 'total_chapters': 0, 'completed_chapters': 0}
    
    def _get_exam_trend_features(self, user_data: Dict) -> Dict[str, Any]:
        """Analyze exam score trends and momentum"""
        try:
            exam_results = user_data.get('exam_results', [])
            
            logger.info(f"    📈 Found {len(exam_results)} exam results")
            
            if len(exam_results) < 2:
                return {
                    'recent_scores': [],
                    'avg_score': 0,
                    'momentum': 0,
                    'score_trend': 'insufficient_data'
                }
            
            # Sort by date and get last 4 exams
            sorted_results = sorted(exam_results, key=lambda x: x.get('exam_date', ''), reverse=True)[:4]
            recent_scores = []
            
            for result in sorted_results:
                try:
                    score = 0
                    if 'percentage' in result:
                        score = float(result['percentage'])
                        logger.info(f"    📊 Processing exam: {result.get('subject', 'Unknown')} - {score}%")
                    elif 'score' in result and 'max_score' in result:
                        score = (float(result['score']) / float(result['max_score'])) * 100
                        logger.info(f"    📊 Processing exam: {result.get('subject', 'Unknown')} - {result.get('score', 0)}/{result.get('max_score', 0)} = {score:.1f}%")
                    else:
                        logger.info(f"    ⚠️  No valid score data in: {result}")
                        continue
                    recent_scores.append(score)
                    logger.info(f"    ✅ Added score: {score:.1f}")
                except Exception as e:
                    logger.error(f"    ❌ Error processing exam result: {e}")
                    continue
            
            if len(recent_scores) < 2:
                return {
                    'recent_scores': recent_scores,
                    'avg_score': 0,
                    'momentum': 0,
                    'score_trend': 'insufficient_data'
                }
            
            # Calculate metrics
            avg_score = sum(recent_scores) / len(recent_scores)
            
            # Momentum: difference between oldest and newest
            momentum = recent_scores[0] - recent_scores[-1]  # newest - oldest
            
            # Trend classification
            if momentum > 5:
                score_trend = 'improving'
            elif momentum < -5:
                score_trend = 'declining'
            else:
                score_trend = 'stable'
            
            return {
                'recent_scores': recent_scores,
                'avg_score': round(avg_score, 1),
                'momentum': round(momentum, 1),
                'score_trend': score_trend
            }
            
        except Exception as e:
            logger.error(f"Error getting exam trend features: {str(e)}")
            return {'recent_scores': [], 'avg_score': 0, 'momentum': 0, 'score_trend': 'error'}
    
    def _get_quiz_test_features(self, uid: str) -> Dict[str, Any]:
        """Analyze quiz and test attempt performance"""
        try:
            attempts_ref = db.collection('users').document(uid).collection('quiz_attempts') \
                .order_by('completed_at', direction=firestore.Query.DESCENDING).stream()

            all_attempts = []
            for doc in attempts_ref:
                a = doc.to_dict()
                if a.get('score') is not None:
                    all_attempts.append(a)

            if not all_attempts:
                return {
                    'total_attempts': 0,
                    'avg_score': 0,
                    'recent_scores': [],
                    'quiz_momentum': 0,
                    'score_by_subject': {},
                    'quiz_vs_mock': {'quiz_avg': 0, 'mock_avg': 0},
                    'total_questions_answered': 0,
                    'overall_quiz_accuracy': 0,
                    'last_quiz_date': None
                }

            total_attempts = len(all_attempts)
            all_scores = [a['score'] for a in all_attempts]
            avg_score = round(sum(all_scores) / len(all_scores), 1)

            recent_8 = all_attempts[:8]
            recent_scores = [round(a['score'], 1) for a in recent_8]

            quiz_momentum = 0
            if len(recent_8) >= 4:
                last_4_avg = sum(a['score'] for a in recent_8[:4]) / 4
                prev_4_avg = sum(a['score'] for a in recent_8[4:]) / len(recent_8[4:])
                quiz_momentum = round(last_4_avg - prev_4_avg, 1)

            subject_scores: Dict[str, list] = {}
            for a in all_attempts:
                subj = a.get('subject') or a.get('topic_id', '').split('_')[2] if a.get('topic_id') else 'unknown'
                if subj not in subject_scores:
                    subject_scores[subj] = []
                subject_scores[subj].append(a['score'])
            score_by_subject = {k: round(sum(v) / len(v), 1) for k, v in subject_scores.items()}

            quiz_scores = [a['score'] for a in all_attempts if (a.get('mode') or '').startswith('topic')]
            mock_scores = [a['score'] for a in all_attempts if 'mock' in (a.get('mode') or '').lower()]
            quiz_vs_mock = {
                'quiz_avg': round(sum(quiz_scores) / len(quiz_scores), 1) if quiz_scores else 0,
                'mock_avg': round(sum(mock_scores) / len(mock_scores), 1) if mock_scores else 0
            }

            total_correct = sum(a.get('correct_count', 0) for a in all_attempts)
            total_submitted = sum(a.get('submitted_count', 0) for a in all_attempts)
            overall_accuracy = round((total_correct / total_submitted * 100), 1) if total_submitted > 0 else 0

            last_quiz_date = None
            if all_attempts and all_attempts[0].get('completed_at'):
                try:
                    ct = all_attempts[0]['completed_at']
                    last_quiz_date = ct.isoformat() if hasattr(ct, 'isoformat') else str(ct)
                except:
                    pass

            return {
                'total_attempts': total_attempts,
                'avg_score': avg_score,
                'recent_scores': recent_scores,
                'quiz_momentum': quiz_momentum,
                'score_by_subject': score_by_subject,
                'quiz_vs_mock': quiz_vs_mock,
                'total_questions_answered': total_submitted,
                'overall_quiz_accuracy': overall_accuracy,
                'last_quiz_date': last_quiz_date
            }

        except Exception as e:
            logger.error(f"Error getting quiz test features for {uid}: {str(e)}")
            return {
                'total_attempts': 0, 'avg_score': 0, 'recent_scores': [],
                'quiz_momentum': 0, 'score_by_subject': {}, 'quiz_vs_mock': {'quiz_avg': 0, 'mock_avg': 0},
                'total_questions_answered': 0, 'overall_quiz_accuracy': 0, 'last_quiz_date': None
            }

    def _get_topic_mastery_features(self, uid: str) -> Dict[str, Any]:
        """Analyze per-topic mastery from topic_performance subcollection"""
        try:
            perf_ref = db.collection('users').document(uid).collection('topic_performance').stream()

            topics_data = {}
            for doc in perf_ref:
                topics_data[doc.id] = doc.to_dict()

            if not topics_data:
                return {
                    'total_topics_practiced': 0,
                    'confidence_breakdown': {'confident': 0, 'practiced': 0, 'not_started': 0},
                    'avg_accuracy': 0,
                    'weak_topics': [],
                    'strong_topics': [],
                    'subjects_summary': {}
                }

            confident = sum(1 for t in topics_data.values() if t.get('confidence') == 'confident')
            practiced = sum(1 for t in topics_data.values() if t.get('confidence') == 'practiced')
            not_started = sum(1 for t in topics_data.values() if t.get('confidence') == 'not_started')

            accuracies = [t.get('accuracy', 0) * 100 for t in topics_data.values() if t.get('total_attempted', 0) > 0]
            avg_accuracy = round(sum(accuracies) / len(accuracies), 1) if accuracies else 0

            weak_topics = []
            strong_topics = []
            subjects_map: Dict[str, list] = {}

            for topic_id, tdata in topics_data.items():
                accuracy = tdata.get('accuracy', 0) * 100
                attempted = tdata.get('total_attempted', 0)
                if attempted == 0:
                    continue

                parts = topic_id.split('_')
                subject = parts[2] if len(parts) >= 3 else 'unknown'
                chapter = parts[3] if len(parts) >= 4 else ''
                topic_name = parts[4] if len(parts) >= 5 else ''

                topic_info = {
                    'topic_id': topic_id,
                    'accuracy': round(accuracy, 1),
                    'total_attempted': attempted,
                    'chapter': chapter,
                    'topic_name': topic_name
                }

                if accuracy < 50:
                    weak_topics.append(topic_info)
                elif accuracy >= 80:
                    strong_topics.append(topic_info)

                if subject not in subjects_map:
                    subjects_map[subject] = []
                subjects_map[subject].append(topic_info)

            subjects_summary = {}
            for subj, topic_list in subjects_map.items():
                subj_accuracies = [t['accuracy'] for t in topic_list]
                subjects_summary[subj] = {
                    'topics_practiced': len(topic_list),
                    'avg_accuracy': round(sum(subj_accuracies) / len(subj_accuracies), 1),
                    'weak_count': sum(1 for t in topic_list if t['accuracy'] < 50),
                    'strong_count': sum(1 for t in topic_list if t['accuracy'] >= 80)
                }

            weak_topics.sort(key=lambda x: x['accuracy'])
            strong_topics.sort(key=lambda x: x['accuracy'], reverse=True)

            return {
                'total_topics_practiced': len(topics_data),
                'confidence_breakdown': {
                    'confident': confident,
                    'practiced': practiced,
                    'not_started': not_started
                },
                'avg_accuracy': avg_accuracy,
                'weak_topics': weak_topics[:5],
                'strong_topics': strong_topics[:5],
                'subjects_summary': subjects_summary
            }

        except Exception as e:
            logger.error(f"Error getting topic mastery features for {uid}: {str(e)}")
            return {
                'total_topics_practiced': 0,
                'confidence_breakdown': {'confident': 0, 'practiced': 0, 'not_started': 0},
                'avg_accuracy': 0, 'weak_topics': [], 'strong_topics': [],
                'subjects_summary': {}
            }

    def _get_heatmap_patterns(self, uid: str) -> Dict[str, Any]:
        """Extract study pattern from heatmap data"""
        try:
            # Get last 30 days of sessions for heatmap
            thirty_days_ago = (datetime.utcnow() - timedelta(days=30)).isoformat()
            sessions_ref = db.collection('users').document(uid).collection('study_sessions').where('start_time', '>=', thirty_days_ago).stream()
            
            # Aggregate by weekday and hour
            time_slots = defaultdict(int)
            total_sessions = 0
            
            for session_doc in sessions_ref:
                session_data = session_doc.to_dict()
                local_hour = session_data.get('local_hour')
                local_weekday = session_data.get('local_weekday')
                
                if local_hour is not None and local_weekday is not None:
                    slot_key = f"{local_weekday}-{local_hour}"
                    time_slots[slot_key] += 1
                    total_sessions += 1
            
            if total_sessions == 0:
                return {
                    'peak_times': [],
                    'study_pattern': 'no_data',
                    'consistency_score': 0
                }
            
            # Find top 3 most active time slots
            sorted_slots = sorted(time_slots.items(), key=lambda x: x[1], reverse=True)[:3]
            peak_times = [{"weekday": int(slot.split('-')[0]), "hour": int(slot.split('-')[1]), "count": count} 
                        for slot, count in sorted_slots]
            
            # Determine study pattern
            weekday_sessions = sum(count for slot, count in time_slots.items() if int(slot.split('-')[0]) < 5)  # Mon-Fri
            weekend_sessions = sum(count for slot, count in time_slots.items() if int(slot.split('-')[0]) >= 5)  # Sat-Sun
            
            if weekend_sessions > weekday_sessions * 1.5:
                study_pattern = 'weekend_warrior'
            elif any(slot['hour'] >= 22 for slot in peak_times):
                study_pattern = 'night_owl'
            elif any(6 <= slot['hour'] <= 9 for slot in peak_times):
                study_pattern = 'morning_regular'
            else:
                study_pattern = 'irregular'
            
            # Consistency: distribution across different times
            unique_slots = len(time_slots)
            max_possible_slots = 7 * 24  # 7 days * 24 hours
            consistency_score = (unique_slots / max_possible_slots) * 100
            
            return {
                'peak_times': peak_times,
                'study_pattern': study_pattern,
                'consistency_score': round(consistency_score, 1)
            }
            
        except Exception as e:
            logger.error(f"Error getting heatmap patterns for {uid}: {str(e)}")
            return {'peak_times': [], 'study_pattern': 'error', 'consistency_score': 0}
    
    def at_risk_prompt(self, features: Dict[str, Any]) -> str:
        """Generate prompt for at-risk classification"""
        return f"""
You are an academic analytics expert. Based on the following student data, determine if the student is at risk of falling behind academically.

Student Data:
{json.dumps(features, indent=2)}

CRITICAL RISK THRESHOLDS:
- Overall completion rate < 25% = AUTOMATIC AT_RISK
- Any subject completion rate < 20% = AUTOMATIC AT_RISK  
- Study sessions < 5 in 30 days = AUTOMATIC AT_RISK
- No chapter completion despite 30+ days = AUTOMATIC AT_RISK

RISK CLASSIFICATION RULES:
1. If overall_completion < 25.0% → MUST classify as "at_risk"
2. If any subject completion < 20.0% → MUST classify as "at_risk"
3. If session_count_30d < 5 → MUST classify as "at_risk"
4. Only classify as "not_at_risk" if ALL conditions are met:
   * Overall completion ≥ 40%
   * All subjects ≥ 25% completion
   * Study sessions ≥ 10 in 30 days
   * Recent academic activity

Login frequency alone does NOT override low academic completion. A student who logs in daily but completes <25% of chapters IS at risk.

Return a JSON response with:
{{
  "risk": "at_risk" or "not_at_risk",
  "explanation": "Brief explanation focusing on completion rates and academic engagement",
  "confidence": 0.0 to 1.0,
  "key_factors": ["factor1", "factor2"] // Main factors influencing decision
}}

PRIORITIZE ACADEMIC COMPLETION OVER LOGIN ACTIVITY. Low completion = AT RISK, regardless of login frequency.
"""
    
    def readiness_prompt(self, features: Dict[str, Any]) -> str:
        """Generate prompt for readiness scoring"""
        return f"""
You are an academic readiness expert. Based on the following student data, calculate their academic readiness score (0-100) and provide a summary assessment.

Student Data:
{json.dumps(features, indent=2)}

Consider ALL of the following:
- Overall academic progress and chapter completion rates
- Recent exam performance trends and momentum
- Quiz/test performance: volume of attempts, average scores, momentum, and accuracy
- Topic-level mastery: confident vs weak topics, subject-wise accuracy
- Study consistency and patterns
- Subject-specific strengths and weaknesses
- Gap between exam scores and quiz scores (exam pressure vs practice comfort)
- Practice coverage breadth (how many topics have been attempted vs total syllabus)
- Ratio of strong topics to weak topics

Return a JSON response with:
{{
  "readiness_score": 0-100,
  "summary": "Brief assessment of readiness (2-3 sentences)",
  "strengths": ["strength1", "strength2"],
  "areas_for_improvement": ["area1", "area2"],
  "subject_insights": {{"subject": "Physics", "status": "strong/average/weak", "focus": "specific topic"}}
}}

Be encouraging but realistic. The score should reflect true preparedness based on both exam performance AND quiz/topic-level practice data.
"""
    
    def clustering_prompt(self, class_students_data: List[Dict[str, Any]]) -> str:
        """Generate prompt for study pattern clustering"""
        # Summarize each student for the prompt
        student_summaries = []
        for student in class_students_data:
            quiz_data = student.get('quiz_tests', {})
            topic_data = student.get('topic_mastery', {})
            summary = {
                'uid': student['uid'],
                'name': student['name'],
                'study_pattern': student.get('heatmap_patterns', {}).get('study_pattern', 'unknown'),
                'consistency_score': student.get('heatmap_patterns', {}).get('consistency_score', 0),
                'peak_times': student.get('heatmap_patterns', {}).get('peak_times', [])[:2],
                'session_frequency': student.get('study_sessions', {}).get('session_count_30d', 0),
                'total_study_time': student.get('study_sessions', {}).get('total_duration_30d', 0),
                'chapter_completion': student.get('chapter_completion', {}).get('overall_completion', 0),
                'completed_chapters': student.get('chapter_completion', {}).get('completed_chapters', 0),
                'total_chapters': student.get('chapter_completion', {}).get('total_chapters', 0),
                'avg_exam_score': student.get('exam_trends', {}).get('avg_score', 0),
                'exam_trend': student.get('exam_trends', {}).get('score_trend', 'no_data'),
                'recent_exam_count': len(student.get('exam_trends', {}).get('recent_scores', [])),
                'total_quiz_attempts': quiz_data.get('total_attempts', 0),
                'avg_quiz_score': quiz_data.get('avg_score', 0),
                'quiz_momentum': quiz_data.get('quiz_momentum', 0),
                'total_topics_practiced': topic_data.get('total_topics_practiced', 0),
                'topics_confident': topic_data.get('confidence_breakdown', {}).get('confident', 0),
                'topics_weak': topic_data.get('confidence_breakdown', {}).get('not_started', 0),
                'topic_mastery_accuracy': topic_data.get('avg_accuracy', 0)
            }
            student_summaries.append(summary)
        
        return f"""
You are an educational data scientist specializing in study pattern analysis. Based on the following class data, identify natural clusters of students with similar study habits.

Class Student Data:
{json.dumps(student_summaries, indent=2)}

Analyze patterns like:
- Study timing preferences (morning, afternoon, evening, late night)
- Consistency levels
- Weekend vs weekday preferences
- Study frequency patterns
- Academic performance (chapter completion, exam scores)
- Study effectiveness (time spent vs results)

Return a JSON response with an array of clusters:
{{
  "clusters": [
    {{
      "label": "Descriptive cluster name (e.g., 'Night Owls', 'Morning Regulars')",
      "description": "Brief description of this group's study habits",
      "student_uids": ["uid1", "uid2"],
      "common_characteristics": ["characteristic1", "characteristic2"],
      "performance_note": "General observation about this group's academic performance"
    }}
  ]
}}

Create 3-5 meaningful clusters that capture the main study patterns in the class.
"""
    
    def call_gemini_with_rate_limit(self, prompt: str, retries: int = 3) -> Optional[Dict[str, Any]]:
        """Call Gemini API with improved rate limiting and dynamic model switching"""
        if not self.ai_available:
            logger.warning("Gemini AI not available for analytics")
            return None
        
        def _make_api_call():
            # Try to get a working model first for rate limiter tracking
            model = self._get_working_model()
            if not model:
                raise Exception("No working AI models available")
            
            model_name = getattr(model, '_model_name', 'unknown')
            
            # Wait if we've made too many calls recently
            rate_limiter.wait_if_needed(model_name=model_name)
            
            for attempt in range(retries):
                try:
                    # Add initial delay for first attempt to avoid immediate rate limiting
                    if attempt == 0:
                        time.sleep(0.5)
                    
                    # Use the model to call Gemini
                    chat = model.start_chat(history=[])
                    response = chat.send_message(prompt, stream=False)
                    
                    if response and hasattr(response, 'text'):
                        # Reset cooldown on successful call
                        rate_limiter.reset_cooldown()
                        
                        # Parse JSON response
                        try:
                            # Extract JSON from response text
                            response_text = response.text.strip()
                            
                            # Handle responses with explanatory text + JSON code blocks
                            if '```json' in response_text:
                                # Extract JSON code block
                                start_idx = response_text.find('```json') + 7
                                end_idx = response_text.find('```', start_idx)
                                if end_idx != -1:
                                    response_text = response_text[start_idx:end_idx].strip()
                            elif response_text.startswith('```json'):
                                # Handle case where response starts with ```json
                                response_text = response_text[7:-3]  # Remove ```json and ```
                            elif response_text.startswith('{') and response_text.endswith('}'):
                                # Direct JSON response
                                pass  # Use as-is
                            else:
                                # Try to find JSON in the text
                                import re
                                json_pattern = r'\{[\s\S]*\}'
                                match = re.search(json_pattern, response_text)
                                if match:
                                    response_text = match.group(0)
                            
                            return json.loads(response_text)
                        except json.JSONDecodeError as e:
                            logger.error(f"Failed to parse Gemini JSON response: {e}")
                            logger.error(f"Response text: {response.text}")
                            if attempt < retries - 1:
                                time.sleep(2)  # Wait before retry on parse error
                            continue
                    else:
                        logger.error("Empty response from Gemini")
                        if attempt < retries - 1:
                            time.sleep(2)  # Wait before retry on empty response
                        continue
                        
                except Exception as e:
                    error_msg = str(e).lower()
                    
                    # Check for rate limit errors
                    if 'rate limit' in error_msg or 'quota' in error_msg or '429' in error_msg or 'resource exhausted' in error_msg:
                        # Mark current model as exhausted and try next
                        self._mark_model_exhausted()
                        logger.warning(f"Model exhausted, switching to next available model")
                        
                        # Trigger quota cooldown
                        rate_limiter.trigger_quota_cooldown(duration_seconds=300)
                        
                        # More conservative exponential backoff: 5s, 10s, 20s
                        wait_time = 5 * (2 ** attempt)
                        logger.warning(f"Rate limit hit, waiting {wait_time}s before retry {attempt + 1}")
                        time.sleep(wait_time)
                        
                        # Try to get a new model for next attempt
                        model = self._get_working_model()
                        if not model:
                            raise Exception("No working AI models available after quota error")
                        model_name = getattr(model, '_model_name', 'unknown')
                        
                        continue
                    else:
                        logger.error(f"Gemini API error: {e}")
                        if attempt == retries - 1:
                            raise e  # Re-raise to trigger circuit breaker
                        time.sleep(3)  # Wait 3s for other errors
            
            logger.error(f"Failed to get Gemini response after {retries} attempts")
            raise Exception("All retry attempts failed")
        
        try:
            return circuit_breaker.call(_make_api_call)
        except Exception as e:
            if "Circuit breaker is OPEN" in str(e):
                logger.warning("Circuit breaker prevented API call due to repeated failures")
                return None
            else:
                logger.error(f"API call failed: {e}")
                return None
    
    def process_students_in_batches(self, student_uids: List[str], batch_size: int = 30, 
                                delay_between_batches: float = 3.0) -> List[Dict[str, Any]]:
        """Process students in smaller batches with longer delays to respect rate limits"""
        results = []
        total_batches = (len(student_uids) + batch_size - 1) // batch_size
        
        for i in range(0, len(student_uids), batch_size):
            batch_uids = student_uids[i:i + batch_size]
            batch_num = i // batch_size + 1
            
            logger.info(f"Processing batch {batch_num}/{total_batches} with {len(batch_uids)} students")
            
            batch_results = []
            for uid in batch_uids:
                try:
                    features = self.build_student_features(uid)
                    if features:
                        batch_results.append({'uid': uid, 'features': features})
                except Exception as e:
                    logger.error(f"Error processing student {uid}: {e}")
                    continue
            
            results.extend(batch_results)
            
            # Add longer delay between batches (except last batch)
            if i + batch_size < len(student_uids):
                logger.info(f"Waiting {delay_between_batches}s before next batch...")
                time.sleep(delay_between_batches)
        
        return results
    
    def predict_student_risk_and_readiness(self, uid: str) -> Tuple[Optional[Dict], Optional[Dict]]:
        """Predict both risk and readiness for a student with manual caching"""
        # Check cache first
        cache_key = f"gemini_risk:predict_student_risk_and_readiness:{uid}"
        cached_result = CacheManager.get(cache_key)
        if cached_result:
            return cached_result.get('risk'), cached_result.get('readiness')
        
        # Debug: Starting new AI analysis
        logger.info(f"🤖 STARTING AI ANALYSIS: Student Risk/Readiness Prediction for UID: {uid[:8]}...")
        
        try:
            # Debug: Building student features
            logger.info(f"📊 BUILDING FEATURES: Collecting academic data for student {uid[:8]}...")
            features = self.build_student_features(uid)
            if not features:
                return None, None
            
            # Combine both predictions in one API call to save requests
            combined_prompt = f"""
{self.at_risk_prompt(features)}

---

{self.readiness_prompt(features)}

Return a single JSON response with both predictions:
{{
  "risk_prediction": {{
    "risk": "at_risk" or "not_at_risk",
    "explanation": "Brief explanation",
    "confidence": 0.0 to 1.0,
    "key_factors": ["factor1", "factor2"]
  }},
  "readiness_prediction": {{
    "readiness_score": 0-100,
    "summary": "Brief assessment",
    "strengths": ["strength1", "strength2"],
    "areas_for_improvement": ["area1", "area2"],
    "subject_insights": {{"subject": "Physics", "status": "strong/average/weak", "focus": "specific topic"}}
  }}
}}
"""
            
            response = self.call_gemini_with_rate_limit(combined_prompt)
            
            if response:
                risk_data = response.get('risk_prediction')
                readiness_data = response.get('readiness_prediction')
                
                # Debug: AI analysis completed successfully
                logger.info(f"✅ AI ANALYSIS COMPLETED: Generated predictions for student {uid[:8]}")
                if risk_data:
                    logger.info(f"🔴 RISK PREDICTION: Level {risk_data.get('risk_level', 'Unknown')} - {risk_data.get('confidence', 'Unknown')} confidence")
                if readiness_data:
                    logger.info(f"🟢 READINESS PREDICTION: Score {readiness_data.get('readiness_score', 'Unknown')} - {readiness_data.get('readiness_level', 'Unknown')}")
                
                # Cache the result
                result_to_cache = {'risk': risk_data, 'readiness': readiness_data}
                CacheManager.set(cache_key, result_to_cache, timeout=3600)  # 1 hour cache
                
                return risk_data, readiness_data
            else:
                return None, None
                
        except Exception as e:
            logger.error(f"Error predicting for student {uid}: {e}")
            return None, None
    
    def analyze_class_study_patterns(self, class_id: str) -> List[Dict[str, Any]]:
        """Analyze study patterns for all students in a class with manual caching"""
        # Check cache first
        cache_key = f"gemini_cluster:analyze_class_study_patterns:{class_id}"
        cached_result = CacheManager.get(cache_key)
        if cached_result:
            return cached_result
        
        # Debug: Starting class analysis
        logger.info(f"🤖 STARTING AI ANALYSIS: Class Study Pattern Clustering for Class ID: {class_id[:8]}...")
        
        try:
            # Debug: Getting class information
            logger.info(f"📊 BUILDING FEATURES: Collecting class data for class {class_id[:8]}...")
            # Get class document
            class_doc = db.collection('classes').document(class_id).get()
            if not class_doc.exists:
                return []
            
            class_data = class_doc.to_dict()
            student_uids = class_data.get('student_uids', [])
            
            if not student_uids:
                return []
            
            # Build features for all students in class
            class_students_data = []
            for uid in student_uids:
                features = self.build_student_features(uid)
                if features:
                    features['uid'] = uid
                    class_students_data.append(features)
            
            # Call Gemini for clustering
            prompt = self.clustering_prompt(class_students_data)
            response = self.call_gemini_with_rate_limit(prompt)
            
            if response and 'clusters' in response:
                clusters = response['clusters']
                
                # Debug: Show actual AI response
                logger.info(f"🤖 AI RESPONSE: {json.dumps(response, indent=2)}")
                
                # Debug: Class clustering completed
                logger.info(f"✅ AI ANALYSIS COMPLETED: Generated {len(clusters)} clusters for class {class_id[:8]}")
                for i, cluster in enumerate(clusters):
                    cluster_size = len(cluster.get('student_uids', []))
                    cluster_label = cluster.get('label', 'Unknown')
                    logger.info(f"📊 CLUSTER {i+1}: {cluster_label} - {cluster_size} students")
                
                # Cache the result
                CacheManager.set(cache_key, clusters, timeout=7200)  # 2 hour cache
                
                return clusters
            else:
                return []
                
        except Exception as e:
            logger.error(f"Error analyzing class patterns for {class_id}: {e}")
            return []
    
    def store_student_predictions(self, uid: str, risk_data: Optional[Dict], readiness_data: Optional[Dict]):
        """Store risk and readiness predictions in Firestore"""
        try:
            user_ref = db.collection('users').document(uid)
            timestamp = datetime.utcnow().isoformat()
            
            updates = {}
            
            if risk_data:
                updates['risk_prediction'] = {
                    **risk_data,
                    'last_updated': timestamp,
                    'prompt_version': 'v2'  # Track new prompt version
                }
            
            if readiness_data:
                updates['readiness_prediction'] = {
                    **readiness_data,
                    'last_updated': timestamp,
                    'prompt_version': 'v2'  # Track new prompt version
                }
            
            if updates:
                user_ref.update(updates)
                logger.info(f"Stored predictions for student {uid}")
            
        except Exception as e:
            logger.error(f"Error storing predictions for {uid}: {e}")
    
    def store_class_clusters(self, class_id: str, clusters: List[Dict[str, Any]]):
        """Store study pattern clusters in Firestore"""
        try:
            class_ref = db.collection('classes').document(class_id)
            timestamp = datetime.utcnow().isoformat()
            
            cluster_data = {
                'study_clusters': clusters,
                'last_clustered': timestamp
            }
            
            class_ref.update(cluster_data)
            logger.info(f"Stored {len(clusters)} clusters for class {class_id}")
            
        except Exception as e:
            logger.error(f"Error storing clusters for class {class_id}: {e}")


# Global instance
gemini_analytics = GeminiAnalytics()
