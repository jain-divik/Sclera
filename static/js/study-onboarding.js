/**
 * Study Mode Onboarding System
 * Provides contextual tutorial for the study timer and productivity features
 */

class StudyOnboardingManager {
    constructor() {
        this.currentStep = 0;
        this.isActive = false;
        this.tutorialSteps = [];
        this.overlay = null;
        this.callout = null;
        this.hasCompletedTutorial = this.checkTutorialStatus();

        this.init();
    }

    init() {
        // Check if tutorial should start from URL parameter
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('tutorial') === 'start') {
            // Remove the parameter from URL
            window.history.replaceState({}, document.title, window.location.pathname);
            // Start tutorial immediately
            setTimeout(() => this.startTutorial(), 500);
            return;
        }

        // Check if this is first visit to study mode and tutorial not completed
        const isFirstStudyVisit = !localStorage.getItem('sclera_study_visited');

        if (isFirstStudyVisit && !this.hasCompletedTutorial) {
            localStorage.setItem('sclera_study_visited', 'true');
            // Show welcome modal after a brief delay
            setTimeout(() => this.showWelcomeModal(), 800);
        }

        // Listen for manual tutorial start
        window.addEventListener('startStudyTutorial', () => this.startTutorial());
    }

    checkTutorialStatus() {
        // Check localStorage status
        const localStatus = localStorage.getItem('sclera_study_tutorial_completed');
        return localStatus === 'true';
    }

    showWelcomeModal() {
        const modal = document.createElement('div');
        modal.className = 'onboarding-modal-overlay';
        modal.innerHTML = `
            <div class="onboarding-modal">
                <div class="onboarding-modal-header">
                    <span class="material-symbols-outlined" style="font-size: 3rem; color: var(--accent);">timer</span>
                    <h2>Welcome to Study Mode!</h2>
                    <p>Your focused productivity environment</p>
                </div>
                <div class="onboarding-modal-body">
                    <p>Study Mode helps you maintain focus and track your learning sessions with intelligent time management and productivity insights.</p>
                    <div class="onboarding-features">
                        <div class="onboarding-feature">
                            <span class="material-symbols-outlined">schedule</span>
                            <span>Pomodoro Timer</span>
                        </div>
                        <div class="onboarding-feature">
                            <span class="material-symbols-outlined">analytics</span>
                            <span>Time Tracking</span>
                        </div>
                        <div class="onboarding-feature">
                            <span class="material-symbols-outlined">task_alt</span>
                            <span>Task Management</span>
                        </div>
                        <div class="onboarding-feature">
                            <span class="material-symbols-outlined">auto_awesome</span>
                            <span>Focus Insights</span>
                        </div>
                    </div>
                </div>
                <div class="onboarding-modal-footer">
                    <button class="onboarding-btn onboarding-btn-secondary" onclick="studyOnboardingManager.skipTutorial()">
                        Skip for now
                    </button>
                    <button class="onboarding-btn onboarding-btn-primary" onclick="studyOnboardingManager.startTutorial()">
                        Start Tutorial
                    </button>
                </div>
            </div>
        `;

        document.body.appendChild(modal);

        // Animate in
        setTimeout(() => modal.classList.add('active'), 10);
    }

    startTutorial() {
        // Close welcome modal if open
        const modal = document.querySelector('.onboarding-modal-overlay');
        if (modal) {
            modal.classList.remove('active');
            setTimeout(() => modal.remove(), 300);
        }

        // Load tutorial steps
        this.tutorialSteps = this.getTutorialSteps();
        this.currentStep = 0;
        this.isActive = true;

        // Add class to body for blur effect
        document.body.classList.add('onboarding-active');

        // Create overlay and callout elements
        this.createOverlay();
        this.createCallout();

        // Start the tour
        setTimeout(() => this.showStep(0), 500);
    }

    getTutorialSteps() {
        // Define all tutorial steps for study mode
        return [
            {
                target: '#timeDisplay',
                title: 'Timer Display',
                description: 'This is your main timer. It shows the remaining time in your current study session. The ring visually represents your progress.',
                position: 'bottom'
            },
            {
                target: '#startBtn',
                title: 'Start Timer',
                description: 'Click here to begin your study session. The timer will automatically start tracking your study time and enable session recording.',
                position: 'top',
                highlight: 'action'
            },
            {
                target: '#pauseBtn',
                title: 'Pause Timer',
                description: 'Pause the timer when you need to take a break. This also pauses session tracking, so your break time won\'t affect your study metrics.',
                position: 'top',
                highlight: 'action'
            },
            {
                target: '#resetBtn',
                title: 'Reset Timer',
                description: 'Reset the timer back to 25 minutes without ending your session. Perfect for starting a new Pomodoro cycle while staying in the same study session.',
                position: 'top',
                highlight: 'action'
            },
            {
                target: '#add5Btn, #add15Btn',
                title: 'Add Time',
                description: 'Need more time? Add 5 or 15 minutes to your current session. Great for when you\'re in a productive flow!',
                position: 'top',
                highlight: 'action'
            },
            {
                target: '#stopSessionContainer',
                title: 'Stop Session',
                description: 'When you\'re completely done studying, use this button to end your session. It stops the timer, resets it, and ends time tracking.',
                position: 'top',
                highlight: 'action'
            },
            {
                target: '.todo-list',
                title: 'Study Tasks',
                description: 'Manage your study tasks here. Add items you want to focus on during your session, and mark them complete as you finish.',
                position: 'left'
            },
            {
                target: '#todoForm',
                title: 'Add Tasks',
                description: 'Quickly add new study tasks to keep your session organized and focused on specific learning objectives.',
                position: 'top',
                highlight: 'action'
            },
            {
                target: '#fullscreenBtn',
                title: 'Fullscreen Mode',
                description: 'Enter distraction-free fullscreen mode for maximum focus. Your timer and tasks fill the entire screen.',
                position: 'left',
                highlight: 'action'
            }
        ];
    }

    createOverlay() {
        this.overlay = document.createElement('div');
        this.overlay.className = 'onboarding-overlay';
        document.body.appendChild(this.overlay);

        // Animate in
        setTimeout(() => this.overlay.classList.add('active'), 10);
    }

    createCallout() {
        this.callout = document.createElement('div');
        this.callout.className = 'onboarding-callout';
        this.callout.innerHTML = `
            <div class="onboarding-callout-header">
                <h3 class="onboarding-callout-title"></h3>
                <button class="onboarding-callout-close" onclick="studyOnboardingManager.endTutorial()">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            <div class="onboarding-callout-body">
                <p class="onboarding-callout-description"></p>
            </div>
            <div class="onboarding-callout-footer">
                <div class="onboarding-progress">
                    <span class="onboarding-progress-text">Step <span class="current-step">1</span> of <span class="total-steps">0</span></span>
                    <div class="onboarding-progress-bar">
                        <div class="onboarding-progress-fill"></div>
                    </div>
                </div>
                <div class="onboarding-callout-actions">
                    <button class="onboarding-btn onboarding-btn-secondary onboarding-btn-prev" onclick="studyOnboardingManager.previousStep()">
                        Previous
                    </button>
                    <button class="onboarding-btn onboarding-btn-primary onboarding-btn-next" onclick="studyOnboardingManager.nextStep()">
                        Next
                    </button>
                </div>
            </div>
        `;

        document.body.appendChild(this.callout);
    }

    showStep(stepIndex) {
        if (stepIndex < 0 || stepIndex >= this.tutorialSteps.length) {
            this.endTutorial();
            return;
        }

        this.currentStep = stepIndex;
        const step = this.tutorialSteps[stepIndex];
        const targetElement = document.querySelector(step.target);

        if (!targetElement) {
            // Skip to next step if target not found
            this.nextStep();
            return;
        }

        // Update callout content
        this.callout.querySelector('.onboarding-callout-title').textContent = step.title;
        this.callout.querySelector('.onboarding-callout-description').textContent = step.description;
        this.callout.querySelector('.current-step').textContent = stepIndex + 1;
        this.callout.querySelector('.total-steps').textContent = this.tutorialSteps.length;

        // Update progress bar
        const progress = ((stepIndex + 1) / this.tutorialSteps.length) * 100;
        this.callout.querySelector('.onboarding-progress-fill').style.width = `${progress}%`;

        // Update button states
        const prevBtn = this.callout.querySelector('.onboarding-btn-prev');
        const nextBtn = this.callout.querySelector('.onboarding-btn-next');

        prevBtn.disabled = stepIndex === 0;
        prevBtn.style.opacity = stepIndex === 0 ? '0.5' : '1';

        if (stepIndex === this.tutorialSteps.length - 1) {
            nextBtn.textContent = 'Finish';
        } else {
            nextBtn.textContent = 'Next';
        }

        // Highlight target element
        this.highlightElement(targetElement, step);

        // Position callout
        this.positionCallout(targetElement, step.position);

        // Scroll element into view
        targetElement.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Animate callout in
        this.callout.classList.add('active');
    }

    highlightElement(element, step) {
        // Remove previous highlights
        document.querySelectorAll('.onboarding-highlight').forEach(el => {
            el.classList.remove('onboarding-highlight', 'onboarding-highlight-notch', 'onboarding-highlight-action');
        });

        // Add highlight to current element
        element.classList.add('onboarding-highlight');

        if (step.highlight === 'notch') {
            element.classList.add('onboarding-highlight-notch');
        } else if (step.highlight === 'action') {
            element.classList.add('onboarding-highlight-action');
        }
    }

    positionCallout(targetElement, position) {
        const targetRect = targetElement.getBoundingClientRect();
        const calloutRect = this.callout.getBoundingClientRect();
        const spacing = 20;

        let top, left;

        switch (position) {
            case 'top':
                top = targetRect.top - calloutRect.height - spacing;
                left = targetRect.left + (targetRect.width / 2) - (calloutRect.width / 2);
                this.callout.setAttribute('data-position', 'top');
                break;
            case 'bottom':
                top = targetRect.bottom + spacing;
                left = targetRect.left + (targetRect.width / 2) - (calloutRect.width / 2);
                this.callout.setAttribute('data-position', 'bottom');
                break;
            case 'left':
                top = targetRect.top + (targetRect.height / 2) - (calloutRect.height / 2);
                left = targetRect.left - calloutRect.width - spacing;
                this.callout.setAttribute('data-position', 'left');
                break;
            case 'right':
                top = targetRect.top + (targetRect.height / 2) - (calloutRect.height / 2);
                left = targetRect.right + spacing;
                this.callout.setAttribute('data-position', 'right');
                break;
            default:
                top = targetRect.bottom + spacing;
                left = targetRect.left + (targetRect.width / 2) - (calloutRect.width / 2);
                this.callout.setAttribute('data-position', 'bottom');
        }

        // Keep callout within viewport
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;

        if (left < spacing) left = spacing;
        if (left + calloutRect.width > viewportWidth - spacing) {
            left = viewportWidth - calloutRect.width - spacing;
        }
        if (top < spacing) top = spacing;
        if (top + calloutRect.height > viewportHeight - spacing) {
            top = viewportHeight - calloutRect.height - spacing;
        }

        this.callout.style.top = `${top}px`;
        this.callout.style.left = `${left}px`;
    }

    nextStep() {
        if (this.currentStep < this.tutorialSteps.length - 1) {
            this.callout.classList.remove('active');
            setTimeout(() => this.showStep(this.currentStep + 1), 300);
        } else {
            this.completeTutorial();
        }
    }

    previousStep() {
        if (this.currentStep > 0) {
            this.callout.classList.remove('active');
            setTimeout(() => this.showStep(this.currentStep - 1), 300);
        }
    }

    skipTutorial() {
        const modal = document.querySelector('.onboarding-modal-overlay');
        if (modal) {
            modal.classList.remove('active');
            setTimeout(() => modal.remove(), 300);
        }

        // Mark as skipped (can be restarted)
        localStorage.setItem('sclera_study_tutorial_skipped', 'true');
    }

    endTutorial() {
        this.isActive = false;

        document.body.classList.remove('onboarding-active');
        // Remove highlights
        document.querySelectorAll('.onboarding-highlight').forEach(el => {
            el.classList.remove('onboarding-highlight', 'onboarding-highlight-notch', 'onboarding-highlight-action');
        });

        // Fade out and remove elements
        if (this.callout) {
            this.callout.classList.remove('active');
            setTimeout(() => this.callout.remove(), 300);
        }

        if (this.overlay) {
            this.overlay.classList.remove('active');
            setTimeout(() => this.overlay.remove(), 300);
        }
    }

    completeTutorial() {
        this.endTutorial();

        // Mark tutorial as completed
        localStorage.setItem('sclera_study_tutorial_completed', 'true');

        // Show completion message
        this.showCompletionMessage();
    }

    showCompletionMessage() {
        const message = document.createElement('div');
        message.className = 'onboarding-completion-message';
        message.innerHTML = `
            <div class="onboarding-completion-content">
                <span class="material-symbols-outlined" style="font-size: 3rem; color: var(--success);">check_circle</span>
                <h3>Ready to Focus!</h3>
                <p>You're all set to use Study Mode effectively. Your time tracking is now active and will help you build better study habits.</p>
            </div>
        `;

        document.body.appendChild(message);

        setTimeout(() => message.classList.add('active'), 10);
        setTimeout(() => {
            message.classList.remove('active');
            setTimeout(() => message.remove(), 300);
        }, 4000);
    }

    restartTutorial() {
        // Clear completion status
        localStorage.removeItem('sclera_study_tutorial_completed');
        localStorage.removeItem('sclera_study_tutorial_skipped');
        this.hasCompletedTutorial = false;

        // Start tutorial
        this.startTutorial();
    }
}

// Initialize study onboarding manager when DOM is ready
let studyOnboardingManager;
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        studyOnboardingManager = new StudyOnboardingManager();
    });
} else {
    studyOnboardingManager = new StudyOnboardingManager();
}
