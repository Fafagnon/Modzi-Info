// ── Navbar scroll effect ──
const navbar = document.querySelector('.navbar');
if (navbar) {
  const checkScroll = () => navbar.classList.toggle('scrolled', window.scrollY > 40);
  window.addEventListener('scroll', checkScroll, { passive: true });
  checkScroll();
}

// ── Mobile menu ──
const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.querySelector('.mobile-menu');
const closeBtn = document.querySelector('.close-btn');
if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => { mobileMenu.classList.add('open'); document.body.style.overflow='hidden'; });
  const close = () => { mobileMenu.classList.remove('open'); document.body.style.overflow=''; };
  if (closeBtn) closeBtn.addEventListener('click', close);
  mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', close));
}

// ── Fade-up animations ──
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
}, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
document.querySelectorAll('.fade-up').forEach(el => io.observe(el));

// ── WhatsApp links ──
function buildWALink(country) {
  const msg = `Bonjour, je suis intéressé(e) par les études en ${country}. Pouvez-vous m'accompagner ?`;
  return `https://wa.me/22899324636?text=${encodeURIComponent(msg)}`;
}
document.querySelectorAll('[data-wa-country]').forEach(el => {
  el.href = buildWALink(el.dataset.waCountry);
  el.target = '_blank'; el.rel = 'noopener noreferrer';
});
document.querySelectorAll('[data-wa-generic]').forEach(el => {
  el.href = 'https://wa.me/22899324636?text=' + encodeURIComponent("Bonjour, j'ai besoin d'aide pour mon projet d'études à l'étranger.");
  el.target = '_blank'; el.rel = 'noopener noreferrer';
});

// ── Smooth scroll ──
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
  });
});

// ── Contact form ──
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', e => {
    e.preventDefault();
    const country = contactForm.querySelector('[name="country"]')?.value || '';
    const name = contactForm.querySelector('[name="name"]')?.value || '';
    const msg = `Bonjour, je m'appelle ${name} et je suis intéressé(e) par les études${country ? ' en ' + country : ' à l\'étranger'}. Pouvez-vous m'accompagner ?`;
    window.open(`https://wa.me/22899324636?text=${encodeURIComponent(msg)}`, '_blank');
  });
}

// ── Counter animation ──
function animateCounter(el) {
  const target = parseInt(el.dataset.counter);
  const suffix = el.dataset.suffix || '';
  let start = null;
  const step = ts => {
    if (!start) start = ts;
    const p = Math.min((ts - start) / 1500, 1);
    el.textContent = Math.floor(p * target) + suffix;
    if (p < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}
const cio = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { animateCounter(e.target); cio.unobserve(e.target); } });
}, { threshold: 0.5 });
document.querySelectorAll('[data-counter]').forEach(el => cio.observe(el));

// ── Article Modals ──
function initModals() {
  // Modal triggers
  document.querySelectorAll('[data-modal]').forEach(trigger => {
    trigger.addEventListener('click', e => {
      e.preventDefault();
      const modalId = trigger.dataset.modal;
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        modal.classList.add('open');
      }
    });
  });

  // Modal close handlers
  document.querySelectorAll('[data-modal-close]').forEach(closeBtn => {
    closeBtn.addEventListener('click', () => {
      const modal = closeBtn.closest('.modal');
      if (modal) {
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        modal.classList.remove('open');
      }
    });
  });

  // Close on Escape key
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      const openModal = document.querySelector('.modal.open');
      if (openModal) {
        openModal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        openModal.classList.remove('open');
      }
    }
  });

  // Close on overlay click
  document.querySelectorAll('.modal__overlay').forEach(overlay => {
    overlay.addEventListener('click', () => {
      const modal = overlay.closest('.modal');
      if (modal) {
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        modal.classList.remove('open');
      }
    });
  });

  // Auto-open modal from URL hash
  const hash = window.location.hash;
  if (hash && hash.startsWith('#modal-')) {
    const modalId = hash.substring(1); // Remove the #
    const modal = document.getElementById(modalId);
    if (modal) {
      setTimeout(() => {
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        modal.classList.add('open');
      }, 500); // Small delay to ensure page is loaded
    }
  }
}

// Initialize modals when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initModals);
} else {
  initModals();
}
