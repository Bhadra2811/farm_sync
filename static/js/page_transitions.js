document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const overlay = document.querySelector('.page-transition-overlay');
    const contentContainer = document.querySelector('.content-container');
    
    setTimeout(function() {
        contentContainer.classList.add('visible');
        overlay.classList.remove('active');
    }, 300);
    
    document.addEventListener('click', function(e) {
        const link = e.target.closest('a');
        if (!link) return;
        
        if (e.ctrlKey || e.shiftKey || e.metaKey || e.altKey) return;
        if (link.target === '_blank') return;
        if (link.hostname !== window.location.hostname) return;
        if (link.getAttribute('href') && link.getAttribute('href').startsWith('#')) return;
        if (link.getAttribute('href') && link.getAttribute('href').startsWith('javascript:')) return;
        
        e.preventDefault();
        overlay.classList.add('active');
        contentContainer.classList.remove('visible');
        
        setTimeout(function() {
            window.location.href = link.href;
        }, 400);
    });
    
    document.querySelectorAll('form').forEach(form => {
        if (form.classList.contains('no-transition')) return;
        
        form.addEventListener('submit', function() {
            overlay.classList.add('active');
            contentContainer.classList.remove('visible');
        });
    });
});

window.addEventListener('pageshow', function(e) {
    if (e.persisted) {
        document.querySelector('.content-container').classList.add('visible');
        document.querySelector('.page-transition-overlay').classList.remove('active');
    }
});