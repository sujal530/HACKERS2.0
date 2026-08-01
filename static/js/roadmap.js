document.addEventListener('DOMContentLoaded', () => {
    // Initialize roadmap interactions and node animations
    initRoadmapAnimations();
    initNodeClickHandlers();
});

/**
 * Handles smooth entry animations for roadmap timeline nodes.
 */
function initRoadmapAnimations() {
    const timelineNodes = document.querySelectorAll('.timeline-node');

    if (timelineNodes.length === 0) {
        return;
    }

    // Intersection Observer to trigger scroll-based node fade-in/slide-in animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const nodeObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    timelineNodes.forEach(node => {
        nodeObserver.observe(node);
    });
}

/**
 * Attaches interactive handlers to individual roadmap nodes.
 */
function initNodeClickHandlers() {
    const timelineNodes = document.querySelectorAll('.timeline-node');

    timelineNodes.forEach(node => {
        node.addEventListener('click', () => {
            // Toggle expansion or highlight active state on user click
            timelineNodes.forEach(n => n.classList.remove('selected-node'));
            node.classList.add('selected-node');
        });
    });
}