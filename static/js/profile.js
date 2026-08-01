document.addEventListener('DOMContentLoaded', () => {
    const profileForm = document.getElementById('profileForm');

    if (profileForm) {
        profileForm.addEventListener('submit', validateProfileForm);
    }
});

/**
 * Validates the profile form fields before submission.
 * @param {Event} event 
 */
function validateProfileForm(event) {
    const careerGoalInput = document.getElementById('career_goal');
    const skillLevelSelect = document.getElementById('skill_level');
    const interestsInput = document.getElementById('interests');
    const dailyAvailableTimeInput = document.getElementById('daily_available_time');
    const learningStyleSelect = document.getElementById('learning_style');

    let isValid = true;
    let errorMessage = '';

    // Validate Career Goal
    if (!careerGoalInput || !careerGoalInput.value.trim()) {
        isValid = false;
        errorMessage = 'Please enter your career goal or primary aspiration.';
    } 
    // Validate Skill Level
    else if (!skillLevelSelect || !skillLevelSelect.value) {
        isValid = false;
        errorMessage = 'Please select your current skill level.';
    } 
    // Validate Interests
    else if (!interestsInput || !interestsInput.value.trim()) {
        isValid = false;
        errorMessage = 'Please enter at least one interest or skill topic.';
    } 
    // Validate Daily Available Time
    else if (!dailyAvailableTimeInput || !dailyAvailableTimeInput.value || parseFloat(dailyAvailableTimeInput.value) <= 0) {
        isValid = false;
        errorMessage = 'Please enter a valid amount of daily available time (greater than 0 hours).';
    } 
    // Validate Learning Style
    else if (!learningStyleSelect || !learningStyleSelect.value) {
        isValid = false;
        errorMessage = 'Please select your preferred learning style.';
    }

    if (!isValid) {
        event.preventDefault();
        alert(errorMessage);
    }
}