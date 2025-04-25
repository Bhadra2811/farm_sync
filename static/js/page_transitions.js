// Page Transitions JavaScript

// Execute when DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const overlay = document.querySelector('.page-transition-overlay');
    const contentContainer = document.querySelector('.content-container');
    
    // Show content with fade-in effect
    setTimeout(function() {
        contentContainer.classList.add('visible');
        overlay.classList.remove('active');
    }, 300);
    
    // Handle all link clicks within the site
    document.addEventListener('click', function(e) {
        const link = e.target.closest('a');
        if (!link) return;
        
        // Skip for special cases
        if (e.ctrlKey || e.shiftKey || e.metaKey || e.altKey) return;
        if (link.target === '_blank') return;
        if (link.hostname !== window.location.hostname) return;
        if (link.getAttribute('href') && link.getAttribute('href').startsWith('#')) return;
        if (link.getAttribute('href') && link.getAttribute('href').startsWith('javascript:')) return;
        
        // Perform transition
        e.preventDefault();
        overlay.classList.add('active');
        contentContainer.classList.remove('visible');
        
        // Navigate after transition
        setTimeout(function() {
            window.location.href = link.href;
        }, 400);
    });
    
    // Handle form submissions
    document.querySelectorAll('form').forEach(form => {
        if (form.classList.contains('no-transition')) return;
        
        form.addEventListener('submit', function() {
            overlay.classList.add('active');
            contentContainer.classList.remove('visible');
        });
    });
});

// Handle browser back/forward navigation
window.addEventListener('pageshow', function(e) {
    if (e.persisted) {
        // Page was loaded from back/forward cache
        document.querySelector('.content-container').classList.add('visible');
        document.querySelector('.page-transition-overlay').classList.remove('active');
    }
});