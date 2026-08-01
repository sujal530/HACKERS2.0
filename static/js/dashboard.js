document.addEventListener('DOMContentLoaded', () => {
    // Fetch initial dynamic dashboard stats if API endpoint is active
    fetchDashboardData();

    // Event listeners for quick interactive elements on dashboard
    initDashboardInteractions();
});

/**
 * Fetches dashboard summary data asynchronously if updated via AJAX.
 */
function fetchDashboardData() {
    // Placeholder for future asynchronous metric updates or chart updates
    const progressElem = document.getElementById('progress-percentage');
    const streakElem = document.getElementById('learning-streak');

    if (progressElem && streakElem) {
        // Log status for development/debugging
        console.log("Dashboard components initialized with values:", {
            progressPercentage: progressElem.innerText,
            learningStreak: streakElem.innerText
        });
    }
}

/**
 * Initializes quick UI listeners for dashboard widgets.
 */
function initDashboardInteractions() {
    const challengeWidget = document.querySelector('.challenge-widget');
    if (challengeWidget) {
        challengeWidget.addEventListener('mouseenter', () => {
            challengeWidget.classList.add('widget-hover');
        });
        challengeWidget.addEventListener('mouseleave', () => {
            challengeWidget.classList.remove('widget-hover');
        });
    }
}