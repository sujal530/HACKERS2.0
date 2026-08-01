document.addEventListener('DOMContentLoaded', () => {
    // Select login and signup forms if present
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');

    if (loginForm) {
        loginForm.addEventListener('submit', handleLoginValidation);
    }

    if (signupForm) {
        signupForm.addEventListener('submit', handleSignupValidation);
    }
});

/**
 * Validates the login form before submission.
 * @param {Event} event 
 */
function handleLoginValidation(event) {
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');

    let isValid = true;
    let errorMessage = '';

    if (!emailInput || !emailInput.value.trim()) {
        isValid = false;
        errorMessage = 'Please enter a valid email address.';
    } else if (!passwordInput || !passwordInput.value.trim()) {
        isValid = false;
        errorMessage = 'Please enter your password.';
    }

    if (!isValid) {
        event.preventDefault();
        alert(errorMessage);
    }
}

/**
 * Validates the signup form before submission.
 * @param {Event} event 
 */
function handleSignupValidation(event) {
    const fullNameInput = document.getElementById('full_name');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');

    let isValid = true;
    let errorMessage = '';

    if (!fullNameInput || !fullNameInput.value.trim()) {
        isValid = false;
        errorMessage = 'Please enter your full name.';
    } else if (!emailInput || !emailInput.value.trim()) {
        isValid = false;
        errorMessage = 'Please enter a valid email address.';
    } else if (!passwordInput || passwordInput.value.trim().length < 6) {
        isValid = false;
        errorMessage = 'Password must be at least 6 characters long.';
    }

    if (!isValid) {
        event.preventDefault();
        alert(errorMessage);
    }
}