#!/usr/bin/env python3
"""
Quick Cache Management CLI for Sclera Academic
Direct cache operations without needing to run the web server
"""
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.cache import (
    clear_ai_cache_for_student,
    clear_ai_cache_for_class, 
    clear_all_ai_cache,
    list_cache_keys,
    clear_cache_for_pattern
)

def check_model_status():
    """Check AI model status"""
    try:
        from gemini_analytics import gemini_analytics
        status = gemini_analytics.get_model_status()
        print("=== AI Model Status ===")
        print(f"Available models: {len(status['available_models'])}")
        for i, model in enumerate(status['available_models']):
            marker = "→ CURRENT" if i == status['current_model_index'] else "  "
            exhausted = " (EXHAUSTED)" if model in status['exhausted_models'] else ""
            print(f"{marker} {model}{exhausted}")
        print(f"Exhausted models: {len(status['exhausted_models'])}")
        print(f"Current model index: {status['current_model_index']}")
    except Exception as e:
        print(f"Error checking model status: {e}")

def reset_models():
    """Reset exhausted AI models"""
    try:
        from gemini_analytics import gemini_analytics
        gemini_analytics.exhausted_models.clear()
        gemini_analytics.current_model_index = 0
        print("✓ AI models reset successfully")
    except Exception as e:
        print(f"Error resetting models: {e}")

def clear_student_analytics_complete(uid):
    """Clear all student analytics data including cache and database records"""
    try:
        from firebase_config import db
        from firebase_admin import firestore
        
        print(f"🧹 Clearing complete analytics for student {uid[:8]}...")
        
        # Clear cache
        clear_ai_cache_for_student(uid)
        print(f"  ✓ Cleared AI cache")
        
        # Clear database records
        student_doc = db.collection('users').document(uid).get()
        if student_doc.exists:
            student_data = student_doc.to_dict()
            name = student_data.get('name', 'Unknown')
            
            # Clear all AI-related fields
            updates = {
                'ai_predictions': firestore.DELETE_FIELD,
                'risk_prediction': firestore.DELETE_FIELD,
                'readiness_prediction': firestore.DELETE_FIELD,
                'risk_analysis': firestore.DELETE_FIELD,
                'readiness_analysis': firestore.DELETE_FIELD,
                'last_analyzed': firestore.DELETE_FIELD,
                'study_clusters': firestore.DELETE_FIELD
            }
            
            db.collection('users').document(uid).update(updates)
            print(f"  ✓ Cleared database records for {name}")
            
        print(f"✅ Complete analytics cleared for student {uid[:8]} ({name})")
        
    except Exception as e:
        print(f"❌ Error clearing student analytics: {e}")

def list_students():
    """List all students with their analytics status"""
    try:
        from firebase_config import db
        
        print("👥 Listing Students:")
        print("=" * 60)
        
        # Get all users who are students
        users_ref = db.collection('users').where('purpose', 'in', ['school', 'exam_prep']).stream()
        
        students = []
        for user_doc in users_ref:
            user_data = user_doc.to_dict()
            uid = user_doc.id
            name = user_data.get('name', 'Unknown')
            
            # Check analytics status
            has_predictions = 'ai_predictions' in user_data
            has_risk = 'risk_prediction' in user_data or 'risk_analysis' in user_data
            has_readiness = 'readiness_prediction' in user_data or 'readiness_analysis' in user_data
            last_analyzed = user_data.get('last_analyzed', 'Never')
            
            analytics_status = "📊" if (has_predictions or has_risk or has_readiness) else "⭕"
            
            students.append({
                'uid': uid,
                'name': name,
                'status': analytics_status,
                'last_analyzed': last_analyzed
            })
        
        # Sort by name
        students.sort(key=lambda x: x['name'])
        
        print(f"Found {len(students)} students:")
        print(f"{'UID':<12} {'Name':<25} {'Analytics':<10} {'Last Analyzed':<20}")
        print("-" * 67)
        
        for student in students:
            print(f"{student['uid'][:12]} {student['name'][:24]:<24} {student['status']:<10} {str(student['last_analyzed'])[:19]:<19}")
        
        return students
        
    except Exception as e:
        print(f"❌ Error listing students: {e}")
        return []

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python cache_cli.py clear-student <uid>           # Clear cache only")
        print("  python cache_cli.py clear-student-full <uid>      # Clear cache + database")
        print("  python cache_cli.py clear-class <class_id>")
        print("  python cache_cli.py clear-all")
        print("  python cache_cli.py list [pattern]")
        print("  python cache_cli.py clear-pattern <pattern>")
        print("  python cache_cli.py students")
        print("  python cache_cli.py model-status")
        print("  python cache_cli.py reset-models")
        return
    
    command = sys.argv[1].lower()
    
    if command == "clear-student":
        if len(sys.argv) < 3:
            print("Error: Student UID required")
            return
        uid = sys.argv[2]
        clear_ai_cache_for_student(uid)
        print(f"✓ Cleared AI cache for student {uid[:8]}...")
    
    elif command == "clear-student-full":
        if len(sys.argv) < 3:
            print("Error: Student UID required")
            return
        uid = sys.argv[2]
        clear_student_analytics_complete(uid)
    
    elif command == "clear-class":
        if len(sys.argv) < 3:
            print("Error: Class ID required")
            return
        class_id = sys.argv[2]
        clear_ai_cache_for_class(class_id)
        print(f"✓ Cleared AI cache for class {class_id[:8]}...")
    
    elif command == "clear-all":
        clear_all_ai_cache()
        print("✓ Cleared all AI cache")
    
    elif command == "list":
        pattern = sys.argv[2] if len(sys.argv) > 2 else None
        keys = list_cache_keys(pattern)
        print(f"Found {len(keys)} cache keys:")
        for key in keys:
            print(f"  {key}")
    
    elif command == "clear-pattern":
        if len(sys.argv) < 3:
            print("Error: Pattern required")
            return
        pattern = sys.argv[2]
        clear_cache_for_pattern(pattern)
        print(f"✓ Cleared cache keys matching pattern: {pattern}")
    
    elif command == "students":
        list_students()
    
    elif command == "model-status":
        check_model_status()
    
    elif command == "reset-models":
        reset_models()
    
    else:
        print(f"Unknown command: {command}")
        print("Available commands: clear-student, clear-student-full, clear-class, clear-all, list, clear-pattern, students, model-status, reset-models")

if __name__ == "__main__":
    main()
