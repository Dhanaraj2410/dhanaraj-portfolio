/* ═══════════════════════════════════════════════════════════════════════════
   AI Resume Analyzer
   ═══════════════════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
  initResumeAnalyzer();
});

function initResumeAnalyzer() {
  const textarea = document.getElementById('analyzer-jd');
  const analyzeBtn = document.getElementById('analyzer-btn');
  const resultsContainer = document.getElementById('analyzer-results');

  if (!analyzeBtn || !textarea) return;

  analyzeBtn.addEventListener('click', async () => {
    const jd = textarea.value.trim();
    if (!jd) {
      alert('Please paste a job description to analyze.');
      return;
    }

    if (jd.length < 20) {
      alert('Job description seems too short. Please provide more detail.');
      return;
    }

    analyzeBtn.disabled = true;
    analyzeBtn.textContent = 'Analyzing...';
    resultsContainer.classList.remove('active');

    try {
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';
      const response = await fetch('/api/ai/resume-analysis/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ job_description: jd }),
      });

      const data = await response.json();

      if (data.success !== false) {
        renderResults(resultsContainer, data);
        resultsContainer.classList.add('active');
      } else {
        alert(data.error || 'Analysis failed. Please try again.');
      }
    } catch (err) {
      alert('Could not complete analysis. Please try again.');
      console.error('Resume analyzer error:', err);
    } finally {
      analyzeBtn.disabled = false;
      analyzeBtn.textContent = '🔍 Analyze Match';
    }
  });
}

function renderResults(container, data) {
  const score = data.match_score || 0;
  const matching = data.matching_skills || [];
  const missing = data.missing_skills || [];
  const projects = data.relevant_projects || [];
  const certs = data.relevant_certifications || [];
  const questions = data.suggested_questions || [];
  const disclaimer = data.disclaimer || 'This is an estimated skill match, not an official ATS score.';

  let scoreColor = 'var(--error)';
  let scoreLabel = 'Needs Improvement';
  if (score >= 80) { scoreColor = 'var(--success)'; scoreLabel = 'Strong Match'; }
  else if (score >= 60) { scoreColor = 'var(--warning)'; scoreLabel = 'Good Match'; }
  else if (score >= 40) { scoreColor = 'var(--info)'; scoreLabel = 'Moderate Match'; }

  container.innerHTML = `
    <div class="card" style="text-align:center; margin-bottom: var(--space-xl);">
      <div class="match-score-circle" style="border-color: ${scoreColor};">
        <div class="match-score-value" style="color: ${scoreColor};">${score}%</div>
      </div>
      <div style="font-size: 1.1rem; font-weight: 700; color: ${scoreColor};">${scoreLabel}</div>
      <p style="font-size: 0.75rem; color: var(--text-muted); margin-top: var(--space-sm);">${disclaimer}</p>
    </div>

    ${matching.length ? `
      <div class="match-section">
        <div class="match-section-title">✅ Matching Skills</div>
        <div class="match-tags">
          ${matching.map(s => `<span class="tech-tag match-tag-yes">✓ ${s}</span>`).join('')}
        </div>
      </div>` : ''}

    ${missing.length ? `
      <div class="match-section">
        <div class="match-section-title">⚠️ Needs Improvement</div>
        <div class="match-tags">
          ${missing.map(s => `<span class="tech-tag match-tag-no">• ${s}</span>`).join('')}
        </div>
      </div>` : ''}

    ${projects.length ? `
      <div class="match-section">
        <div class="match-section-title">🚀 Relevant Projects</div>
        <ul style="list-style: none; padding: 0;">
          ${projects.map(p => `<li style="padding: 0.3rem 0; color: var(--text-secondary);">▸ ${p}</li>`).join('')}
        </ul>
      </div>` : ''}

    ${certs.length ? `
      <div class="match-section">
        <div class="match-section-title">📜 Relevant Certifications</div>
        <ul style="list-style: none; padding: 0;">
          ${certs.map(c => `<li style="padding: 0.3rem 0; color: var(--text-secondary);">▸ ${c}</li>`).join('')}
        </ul>
      </div>` : ''}

    ${questions.length ? `
      <div class="match-section">
        <div class="match-section-title">💡 Suggested Interview Questions</div>
        <ol style="padding-left: 1.2rem; color: var(--text-secondary); font-size: 0.9rem;">
          ${questions.map(q => `<li style="padding: 0.3rem 0;">${q}</li>`).join('')}
        </ol>
      </div>` : ''}
  `;
}
