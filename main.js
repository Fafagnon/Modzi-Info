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
  return `https://wa.me/33675700925?text=${encodeURIComponent(msg)}`;
}
document.querySelectorAll('[data-wa-country]').forEach(el => {
  el.href = buildWALink(el.dataset.waCountry);
  el.target = '_blank'; el.rel = 'noopener noreferrer';
});
document.querySelectorAll('[data-wa-generic]').forEach(el => {
  el.href = 'https://wa.me/33675700925?text=' + encodeURIComponent('Bonjour, Je souhaite en savoir plus sur votre service AVI et ASSISTANCE VISA');
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
    window.open(`https://wa.me/33675700925?text=${encodeURIComponent(msg)}`, '_blank');
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

// ── Swipe & Match Wizard ──
function initWizard() {
  const wizardBtn = document.querySelectorAll('.wizard-btn');
  if (!wizardBtn.length) return;

  const answers = { q1: '', q2: '', q3: '' };
  
  // Scoring points for each country
  const countries = {
    france: { name: 'France', score: 0, desc: "La France est un excellent choix ! Tu pourras étudier en français avec des frais très réduits.", link: 'france.html' },
    allemagne: { name: 'Allemagne', score: 0, desc: "L'Allemagne est ta destination idéale. Elle combine des études quasi-gratuites, une grande reconnaissance mondiale et de formidables opportunités de travail.", link: 'allemagne.html' },
    belgique: { name: 'Belgique', score: 0, desc: "La Belgique t'offre une excellente éducation en français au cœur de l'Europe.", link: 'belgique.html' },
    italie: { name: 'Italie', score: 0, desc: "L'Italie est parfaite pour toi avec son climat agréable, sa riche culture et ses frais de scolarité abordables.", link: 'italie.html' },
    canada: { name: 'Canada', score: 0, desc: "Le Canada est la meilleure option pour construire ton avenir à long terme et y faire carrière, avec la possibilité d'étudier en français ou en anglais.", link: 'canada.html' }
  };

  wizardBtn.forEach(btn => {
    btn.addEventListener('click', () => {
      const q = btn.dataset.question;
      const val = btn.dataset.value;
      answers['q' + q] = val;

      // Logic weighting
      if (q === '1') {
        if (val === 'budget') { countries.allemagne.score += 3; countries.france.score += 2; countries.italie.score += 2; }
        if (val === 'carriere') { countries.canada.score += 3; countries.allemagne.score += 2; }
        if (val === 'prestige') { countries.allemagne.score += 2; countries.canada.score += 2; countries.france.score += 1; }
        if (val === 'facilite') { countries.france.score += 3; countries.belgique.score += 2; countries.canada.score += 1; }
      }
      if (q === '2') {
        if (val === 'fr') { countries.france.score += 3; countries.belgique.score += 3; countries.canada.score += 2; countries.allemagne.score -= 2; }
        if (val === 'en') { countries.allemagne.score += 2; countries.canada.score += 2; countries.italie.score += 1; }
        if (val === 'both') { countries.canada.score += 2; countries.allemagne.score += 1; }
      }
      if (q === '3') {
        if (val === 'low') { countries.italie.score += 2; countries.allemagne.score += 1; countries.france.score += 1; countries.canada.score -= 3; }
        if (val === 'med') { countries.france.score += 1; countries.belgique.score += 1; countries.allemagne.score += 1; }
        if (val === 'high') { countries.canada.score += 3; countries.belgique.score += 1; }
      }

      // Transition to next step
      document.getElementById('wizard-step-' + q).classList.remove('active');
      const nextQ = parseInt(q) + 1;
      const progress = (nextQ - 1) * 33.33;
      document.getElementById('wizard-progress-bar').style.width = progress + '%';

      if (nextQ <= 3) {
        document.getElementById('wizard-step-' + nextQ).classList.add('active');
      } else {
        // Show result
        document.getElementById('wizard-result').classList.add('active');
        setTimeout(() => {
          document.getElementById('wizard-loader').style.display = 'none';
          document.getElementById('wizard-match-content').style.display = 'block';
          
          // Find winner
          let winnerKey = Object.keys(countries).reduce((a, b) => countries[a].score > countries[b].score ? a : b);
          let winner = countries[winnerKey];
          
          // Calculate a fake percentage (75% to 98%)
          let maxScore = 9; // Approx max possible
          let percentage = Math.min(98, Math.max(75, Math.round((winner.score / maxScore) * 100) + 10));

          document.getElementById('match-score').innerText = percentage;
          document.getElementById('match-country-name').innerText = winner.name;
          document.getElementById('match-country-desc').innerText = winner.desc;
          document.getElementById('match-country-link').href = winner.link;
        }, 1500);
      }
    });
  });

  document.getElementById('wizard-restart')?.addEventListener('click', () => {
    // Reset scores
    Object.keys(countries).forEach(k => countries[k].score = 0);
    document.getElementById('wizard-result').classList.remove('active');
    document.getElementById('wizard-match-content').style.display = 'none';
    document.getElementById('wizard-loader').style.display = 'flex';
    document.getElementById('wizard-progress-bar').style.width = '33.33%';
    document.getElementById('wizard-step-1').classList.add('active');
  });
}

// ── Gauges Animation ──
function initGaugesAnimation() {
  const gauges = document.querySelectorAll('.gauge-fill');
  if (gauges.length === 0) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const fill = entry.target;
        const score = fill.dataset.score;
        setTimeout(() => {
          fill.style.width = score + '%';
        }, 150);
        obs.unobserve(fill);
      }
    });
  }, { threshold: 0.2 });

  gauges.forEach(g => observer.observe(g));
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    initModals();
    initWizard();
    initGaugesAnimation();
    initTestimonialsCarousel();
  });
} else {
  initModals();
  initWizard();
  initGaugesAnimation();
  initTestimonialsCarousel();
}

// ── Testimonials Carousel ──
function initTestimonialsCarousel() {
  const slider = document.getElementById('testimonials-slider');
  const prevBtn = document.querySelector('.prev-btn');
  const nextBtn = document.querySelector('.next-btn');

  if (slider && prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => {
      const cardWidth = slider.querySelector('.testimonial-card').offsetWidth + 28;
      slider.scrollBy({ left: -cardWidth, behavior: 'smooth' });
    });

    nextBtn.addEventListener('click', () => {
      const cardWidth = slider.querySelector('.testimonial-card').offsetWidth + 28;
      slider.scrollBy({ left: cardWidth, behavior: 'smooth' });
    });
  }
}

