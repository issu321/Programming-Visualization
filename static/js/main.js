/**
 * Programming Visualization Platform - Main JavaScript
 * Developed by issu321
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize particles
    initParticles();

    // Initialize navbar
    initNavbar();

    // Initialize theme toggle
    initThemeToggle();

    // Initialize flash auto-dismiss
    initFlashDismiss();

    // Initialize mobile menu
    initMobileMenu();

    // Initialize animations
    initScrollAnimations();
});

// Particle System
function initParticles() {
    const container = document.getElementById('particles');
    if (!container) return;

    const particleCount = 25;
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 15 + 's';
        particle.style.animationDuration = (10 + Math.random() * 10) + 's';
        particle.style.opacity = 0.1 + Math.random() * 0.3;
        container.appendChild(particle);
    }
}

// Navbar scroll effect
function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.2)';
        } else {
            navbar.style.boxShadow = 'none';
        }

        lastScroll = currentScroll;
    });
}

// Theme Toggle
function initThemeToggle() {
    const toggle = document.getElementById('themeToggle');
    if (!toggle) return;

    const html = document.documentElement;

    // Load saved theme
    const savedTheme = localStorage.getItem('theme') || 'dark';
    html.setAttribute('data-theme', savedTheme);

    toggle.addEventListener('click', async () => {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        // Update Mermaid theme if present
        if (typeof mermaid !== 'undefined') {
            mermaid.initialize({
                theme: newTheme === 'dark' ? 'dark' : 'default'
            });
        }

        // Update Plotly charts
        updatePlotlyTheme(newTheme);

        // Sync with server if logged in
        try {
            await fetch('/api/theme', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ theme: newTheme })
            });
        } catch (e) {
            // Silent fail for theme sync
        }
    });
}

function updatePlotlyTheme(theme) {
    const textColor = theme === 'dark' ? '#f1f5f9' : '#0f172a';
    const mutedColor = theme === 'dark' ? '#94a3b8' : '#64748b';
    const gridColor = theme === 'dark' ? 'rgba(255,255,255,0.05)' : 'rgba(0,0,0,0.05)';

    const charts = document.querySelectorAll('.js-plotly-plot');
    charts.forEach(chart => {
        const layout = chart.layout || {};

        // Update all text colors
        layout.paper_bgcolor = 'rgba(0,0,0,0)';
        layout.plot_bgcolor = 'rgba(0,0,0,0)';
        layout.font = { color: textColor, family: 'Inter, sans-serif' };

        // Update title
        if (layout.title) {
            if (typeof layout.title === 'string') {
                layout.title = { text: layout.title, font: { color: textColor, size: 16 } };
            } else if (layout.title.font) {
                layout.title.font.color = textColor;
            }
        }

        // Update axis colors
        ['xaxis', 'yaxis'].forEach(axis => {
            if (layout[axis]) {
                if (layout[axis].title) {
                    if (typeof layout[axis].title === 'string') {
                        layout[axis].title = { text: layout[axis].title, font: { color: mutedColor } };
                    } else if (layout[axis].title.font) {
                        layout[axis].title.font.color = mutedColor;
                    }
                }
                layout[axis].tickfont = { color: mutedColor };
                layout[axis].gridcolor = gridColor;
            }
        });

        // Update legend
        if (layout.legend) {
            layout.legend.font = { color: textColor };
        }

        if (typeof Plotly !== 'undefined') {
            Plotly.relayout(chart, layout);
        }
    });
}

// Flash auto-dismiss
function initFlashDismiss() {
    const flashes = document.querySelectorAll('[data-auto-dismiss]');
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.style.opacity = '0';
            flash.style.transform = 'translateX(100%)';
            setTimeout(() => flash.remove(), 300);
        }, 5000);
    });
}

// Mobile Menu
function initMobileMenu() {
    const toggle = document.getElementById('navToggle');
    const menu = document.getElementById('navMenu');
    if (!toggle || !menu) return;

    toggle.addEventListener('click', () => {
        menu.classList.toggle('active');

        const spans = toggle.querySelectorAll('span');
        if (menu.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!toggle.contains(e.target) && !menu.contains(e.target)) {
            menu.classList.remove('active');
            const spans = toggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
}

// Scroll Animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Animate cards on scroll
    const animateElements = document.querySelectorAll('.feature-card, .stat-card, .viz-card, .tech-item, .feature-detail-card');
    animateElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = `opacity 0.5s ease ${index * 0.05}s, transform 0.5s ease ${index * 0.05}s`;
        observer.observe(el);
    });
}

// Utility: Copy to clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copied to clipboard!', 'success');
    }).catch(() => {
        showToast('Failed to copy', 'error');
    });
}

// Utility: Show toast
function showToast(message, type = 'info') {
    const container = document.querySelector('.flash-container') || document.body;
    const toast = document.createElement('div');
    toast.className = `flash flash-${type}`;
    toast.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
        <span>${message}</span>
        <button class="flash-close" onclick="this.parentElement.remove()">&times;</button>
    `;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Utility: Debounce
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Export for module use if needed
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { initParticles, initThemeToggle, copyToClipboard, showToast };
}
