/* ═══════════════════════════════════════════════════════════════════════════
   DHANARAJ AI/ML PORTFOLIO — Main JavaScript
   Navigation, theme toggle, scroll animations, counters, contact form
   ═══════════════════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initNavigation();
  initScrollAnimations();
  initCounters();
  initContactForm();
  initSkillBars();
  initGitHub();
});

/* ─── Theme Toggle ─────────────────────────────────────────────────────────── */
function initThemeToggle() {
  const toggle = document.getElementById('theme-toggle');
  if (!toggle) return;

  const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(toggle, savedTheme);

  toggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('portfolio-theme', next);
    updateThemeIcon(toggle, next);
  });
}

function updateThemeIcon(toggle, theme) {
  toggle.textContent = theme === 'dark' ? '☀️' : '🌙';
  toggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
}

/* ─── Navigation ───────────────────────────────────────────────────────────── */
function initNavigation() {
  const navbar = document.querySelector('.navbar');
  const hamburger = document.getElementById('nav-hamburger');
  const navLinks = document.getElementById('nav-links');
  const links = document.querySelectorAll('.nav-links a[href^="#"]');

  // Scroll effect
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
        updateActiveLink();
        ticking = false;
      });
      ticking = true;
    }
  });

  // Hamburger toggle
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
  }

  // Smooth scroll for nav links
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href');
      const target = document.querySelector(targetId);
      if (target) {
        const offset = navbar.offsetHeight + 20;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
      // Close mobile menu
      if (hamburger) hamburger.classList.remove('active');
      if (navLinks) navLinks.classList.remove('active');
    });
  });
}

function updateActiveLink() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
  const scrollPos = window.scrollY + 100;

  let currentSection = '';
  sections.forEach(section => {
    if (section.offsetTop <= scrollPos) {
      currentSection = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.classList.toggle('active', link.getAttribute('href') === `#${currentSection}`);
  });
}

/* ─── Scroll Animations ───────────────────────────────────────────────────── */
function initScrollAnimations() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
  );

  document.querySelectorAll('.fade-up, .fade-in, .stagger-children, .timeline-item, .workflow-step').forEach(el => {
    observer.observe(el);
  });
}

/* ─── Animated Counters ────────────────────────────────────────────────────── */
function initCounters() {
  const counters = document.querySelectorAll('[data-counter]');
  if (!counters.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.counted) {
          entry.target.dataset.counted = 'true';
          animateCounter(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  counters.forEach(counter => observer.observe(counter));
}

function animateCounter(el) {
  const target = el.getAttribute('data-counter');
  const isDecimal = target.includes('.');
  const targetNum = parseFloat(target);
  const duration = 1500;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = eased * targetNum;

    if (isDecimal) {
      el.textContent = current.toFixed(2);
    } else {
      el.textContent = Math.floor(current);
    }

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      el.textContent = target;
    }
  }

  requestAnimationFrame(update);
}

/* ─── Skill Bars ───────────────────────────────────────────────────────────── */
function initSkillBars() {
  const bars = document.querySelectorAll('.skill-bar-fill');
  if (!bars.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const width = entry.target.getAttribute('data-width');
          entry.target.style.width = width + '%';
        }
      });
    },
    { threshold: 0.3 }
  );

  bars.forEach(bar => observer.observe(bar));
}

/* ─── Contact Form ─────────────────────────────────────────────────────────── */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const submitBtn = form.querySelector('button[type="submit"]');
    const successMsg = document.getElementById('form-success');
    const originalText = submitBtn.textContent;

    // Disable button
    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending...';

    try {
      const formData = new FormData(form);
      const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

      const response = await fetch('/contact/submit/', {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': csrfToken,
        },
      });

      const data = await response.json();

      if (data.success) {
        form.reset();
        if (successMsg) {
          successMsg.textContent = data.message;
          successMsg.classList.add('active');
          setTimeout(() => successMsg.classList.remove('active'), 5000);
        }
      } else {
        // Show validation errors
        const errors = data.errors || {};
        let errorMsg = 'Please fix the following errors:\n';
        for (const [field, msgs] of Object.entries(errors)) {
          errorMsg += `• ${field}: ${msgs.join(', ')}\n`;
        }
        alert(errorMsg);
      }
    } catch (err) {
      alert('Something went wrong. Please try again later.');
      console.error('Contact form error:', err);
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = originalText;
    }
  });
}

/* ─── GitHub Integration ───────────────────────────────────────────────────── */
function initGitHub() {
  const container = document.getElementById('github-content');
  if (!container) return;

  fetchGitHubData(container);
}

async function fetchGitHubData(container) {
  try {
    const response = await fetch('/api/github/');
    const data = await response.json();

    if (!data.success) {
      container.innerHTML = `
        <div class="text-center" style="color: var(--text-muted); padding: 2rem;">
          <p>GitHub data is currently unavailable.</p>
          <p style="font-size: 0.8rem; margin-top: 0.5rem;">Configure GITHUB_USERNAME in settings to enable.</p>
        </div>`;
      return;
    }

    renderGitHub(container, data);
  } catch (err) {
    console.error('GitHub fetch error:', err);
    container.innerHTML = `
      <div class="text-center" style="color: var(--text-muted); padding: 2rem;">
        <p>Could not load GitHub data.</p>
      </div>`;
  }
}

function renderGitHub(container, data) {
  const profile = data.profile || {};
  const repos = data.repositories || [];
  const languages = data.languages || {};

  // Calculate language bar segments
  const totalLangCount = Object.values(languages).reduce((a, b) => a + b, 0);
  const langColors = {
    'Python': '#3572A5', 'JavaScript': '#f1e05a', 'HTML': '#e34c26',
    'CSS': '#563d7c', 'Java': '#b07219', 'Jupyter Notebook': '#DA5B0B',
    'TypeScript': '#2b7489', 'Shell': '#89e051',
  };

  let langBarHTML = '';
  let langLegendHTML = '';
  for (const [lang, count] of Object.entries(languages).sort((a, b) => b[1] - a[1])) {
    const pct = ((count / totalLangCount) * 100).toFixed(1);
    const color = langColors[lang] || '#8b8b8b';
    langBarHTML += `<div class="lang-bar-segment" style="width:${pct}%;background:${color};" title="${lang} ${pct}%"></div>`;
    langLegendHTML += `<span class="lang-legend-item"><span class="repo-lang-dot" style="background:${color}"></span>${lang} ${pct}%</span>`;
  }

  // Repos HTML (top 6)
  const reposHTML = repos.slice(0, 6).map(repo => {
    const lang = repo.language || '';
    const langClass = `lang-${lang.toLowerCase().replace(/\s+/g, '')}`;
    const updated = repo.updated_at ? new Date(repo.updated_at).toLocaleDateString() : '';
    return `
      <a href="${repo.url}" target="_blank" rel="noopener" class="repo-card">
        <div class="repo-name">📁 ${repo.name}</div>
        <div class="repo-desc">${repo.description || 'No description'}</div>
        <div class="repo-meta">
          ${lang ? `<span><span class="repo-lang-dot ${langClass}"></span> ${lang}</span>` : ''}
          <span>⭐ ${repo.stars}</span>
          <span>🍴 ${repo.forks}</span>
          ${updated ? `<span>📅 ${updated}</span>` : ''}
        </div>
      </a>`;
  }).join('');

  container.innerHTML = `
    <div class="github-header">
      ${profile.avatar_url ? `<img src="${profile.avatar_url}" alt="GitHub Avatar" class="github-avatar">` : ''}
      <div>
        <h3 style="font-size:1.2rem;font-weight:700;">${profile.name || profile.username}</h3>
        <p style="color:var(--text-secondary);font-size:0.9rem;">${profile.bio || ''}</p>
      </div>
      <div class="github-stats">
        <div class="github-stat">
          <div class="github-stat-value">${profile.public_repos || 0}</div>
          <div class="github-stat-label">Repos</div>
        </div>
        <div class="github-stat">
          <div class="github-stat-value">${data.total_stars || 0}</div>
          <div class="github-stat-label">Stars</div>
        </div>
        <div class="github-stat">
          <div class="github-stat-value">${profile.followers || 0}</div>
          <div class="github-stat-label">Followers</div>
        </div>
      </div>
    </div>
    ${Object.keys(languages).length ? `
      <div class="github-languages">
        <div class="lang-bar">${langBarHTML}</div>
        <div class="lang-legend">${langLegendHTML}</div>
      </div>` : ''}
    <div class="github-contribution-card" style="margin-top:var(--space-lg);text-align:center;background:var(--bg-card);padding:1.5rem;border-radius:var(--radius-lg);border:1px solid var(--border-color);">
      <h4 style="margin-bottom:1rem;color:var(--text-primary);font-size:1rem;font-weight:600;">🔥 GitHub Contribution Activity (@${profile.username || 'Dhanaraj2410'})</h4>
      <img src="https://ghchart.rshah.org/4070F4/${profile.username || 'Dhanaraj2410'}" alt="GitHub Contribution Graph" style="width:100%;max-width:750px;border-radius:6px;filter:contrast(1.1);" loading="lazy" />
    </div>
    <div class="repos-grid" style="margin-top:var(--space-xl);">
      ${reposHTML || '<p class="text-center" style="color:var(--text-muted);">No repositories found.</p>'}
    </div>
    <div class="text-center" style="margin-top:var(--space-xl);">
      <a href="${profile.html_url || 'https://github.com/Dhanaraj2410'}" target="_blank" rel="noopener" class="btn btn-outline">
        🐙 View Full GitHub Profile (@Dhanaraj2410) →
      </a>
    </div>`;
}

