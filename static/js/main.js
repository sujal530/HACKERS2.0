document.addEventListener('DOMContentLoaded', () => {
    // Initialize common layout functionality
    initFlashMessageDismissal();
    highlightActiveNavLink();
});

/**
 * Handles automatic and manual dismissal of alert flash messages across pages.
 */
function initFlashMessageDismissal() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach((alert) => {
        // Auto-dismiss flash messages after 5 seconds
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 0.5s ease';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
}

/**
 * Highlights the current active navigation link based on window location.
 */
function highlightActiveNavLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-links a');

    navLinks.forEach((link) => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('active');
        }
    });
}