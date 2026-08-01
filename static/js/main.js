document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------
    // 1. Auth Form Handling (Login & Signup)
    // -------------------------------------------------------------
    const authForm = document.querySelector('#authForm');
    const submitBtn = document.querySelector('#submitBtn');

    if (authForm) {
        authForm.addEventListener('submit', (event) => {
            const emailInput = document.querySelector('input[name="email"]');
            const passwordInput = document.querySelector('input[name="password"]');

            // Client-side quick check
            if (!emailInput.value.trim() || !passwordInput.value.trim()) {
                event.preventDefault(); // Stop form submission if empty
                alert('Please fill in both email and password.');
                return;
            }

            // Optional: Disable button on submit to prevent double-clicks during server delay
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerText = 'Logging in...';
            }
        });
    }

    // -------------------------------------------------------------
    // 2. Auto-hide Flash Messages after 4 seconds
    // -------------------------------------------------------------
    const flashMessages = document.querySelectorAll('.flash-message');
    if (flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach((msg) => {
                msg.style.transition = 'opacity 0.5s ease';
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 500);
            });
        }, 4000);
    }
});