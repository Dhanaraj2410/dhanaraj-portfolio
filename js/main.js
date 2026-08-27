/* =============================================
   MAIN.JS — Navigation, Scroll, Typing, Reveal
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  /* ---------- Navbar Scroll Effect ---------- */
  const navbar = document.getElementById('navbar');
  const handleNavScroll = () => {
    navbar.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', handleNavScroll, { passive: true });
  handleNavScroll();

  /* ---------- Mobile Menu ---------- */
  const burger = document.getElementById('nav-burger');
  const navLinks = document.getElementById('nav-links');
  const navOverlay = document.getElementById('nav-overlay');

  const toggleMobileNav = () => {
    burger.classList.toggle('open');
    navLinks.classList.toggle('open');
    navOverlay.classList.toggle('visible');
    document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
  };

  burger.addEventListener('click', toggleMobileNav);
  navOverlay.addEventListener('click', toggleMobileNav);

  // Close mobile nav when clicking a link
  navLinks.querySelectorAll('.navbar__link').forEach(link => {
    link.addEventListener('click', () => {
      if (navLinks.classList.contains('open')) toggleMobileNav();
    });
  });

  /* ---------- Active Nav Link on Scroll ---------- */
  const sections = document.querySelectorAll('section[id]');
  const navLinkEls = document.querySelectorAll('.navbar__link');

  const updateActiveNav = () => {
    const scrollY = window.scrollY + 120;
    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');
      if (scrollY >= top && scrollY < top + height) {
        navLinkEls.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          }
        });
      }
    });
  };

  window.addEventListener('scroll', updateActiveNav, { passive: true });


  /* ---------- Typing Animation ---------- */
  const roles = [
    'Python Developer',
    'Data Analyst',
    'Data Scientist',
    'Machine Learning Engineer',
    'AI/ML Engineer',
    'Junior AI Engineer',
    'Junior Data Scientist',
    'Python/Django Developer'
  ];

  const typedEl = document.getElementById('typed-role');
  let roleIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typeSpeed = 100;

  function typeRole() {
    const currentRole = roles[roleIndex];

    if (isDeleting) {
      typedEl.textContent = currentRole.substring(0, charIndex - 1);
      charIndex--;
      typeSpeed = 50;
    } else {
      typedEl.textContent = currentRole.substring(0, charIndex + 1);
      charIndex++;
      typeSpeed = 100;
    }

    if (!isDeleting && charIndex === currentRole.length) {
      typeSpeed = 2000; // Pause at end
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      typeSpeed = 400; // Pause before next word
    }

    setTimeout(typeRole, typeSpeed);
  }

  typeRole();


  /* ---------- Scroll Reveal (Intersection Observer) ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  revealEls.forEach(el => revealObserver.observe(el));


  /* ---------- Skills Tabs ---------- */
  const skillTabs = document.querySelectorAll('.skills__tab');
  const skillPanels = document.querySelectorAll('.skills__grid');

  skillTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.dataset.tab;

      skillTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      skillPanels.forEach(panel => {
        panel.classList.remove('active');
        if (panel.dataset.panel === target) {
          panel.classList.add('active');
        }
      });
    });
  });


  /* ---------- Back to Top ---------- */
  const backToTop = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    backToTop.classList.toggle('visible', window.scrollY > 500);
  }, { passive: true });

  backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });


  /* ---------- Copy Email to Clipboard ---------- */
  const copyEmailBtn = document.getElementById('copy-email');
  copyEmailBtn.addEventListener('click', () => {
    navigator.clipboard.writeText('lokhandedhanraj2410@gmail.com')
      .then(() => showToast('📋 Email copied to clipboard!'))
      .catch(() => showToast('❌ Could not copy email'));
  });


  /* ---------- Contact Form Submit (Demo) ---------- */
  const contactForm = document.getElementById('contact-form');
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('cf-name').value.trim();
    if (name) {
      showToast(`Thanks, ${name}! 🎉 Your message was sent (demo).`);
      contactForm.reset();
    }
  });


  /* ---------- Toast Notification ---------- */
  window.showToast = function(message, duration = 3000) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), duration);
  };

  /* ---------- Smooth Scroll for anchor links ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

});
