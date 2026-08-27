/* ═══════════════════════════════════════════════════════════════════════════
   ML Workflow Visualization
   Animated step-by-step pipeline rendering
   ═══════════════════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
  initWorkflowAnimations();
});

function initWorkflowAnimations() {
  const containers = document.querySelectorAll('.workflow-container');
  if (!containers.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const steps = entry.target.querySelectorAll('.workflow-step');
          steps.forEach((step, index) => {
            setTimeout(() => {
              step.classList.add('visible');
            }, index * 200);
          });
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  containers.forEach(container => observer.observe(container));
}

/**
 * Create a generic ML workflow visualization.
 * Used on the homepage for the featured workflow section.
 */
function createGenericWorkflow(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const steps = [
    { icon: '📊', title: 'Data' },
    { icon: '🧹', title: 'Preprocessing' },
    { icon: '📈', title: 'EDA' },
    { icon: '⚙️', title: 'Feature Engineering' },
    { icon: '🧠', title: 'Model Training' },
    { icon: '📋', title: 'Evaluation' },
    { icon: '🚀', title: 'Deployment' },
    { icon: '🎯', title: 'Prediction' },
  ];

  let html = '';
  steps.forEach((step, index) => {
    if (index > 0) {
      html += '<div class="workflow-arrow">→</div>';
    }
    html += `
      <div class="workflow-step">
        <div class="workflow-step-icon">${step.icon}</div>
        <div class="workflow-step-title">${step.title}</div>
      </div>`;
  });

  container.innerHTML = html;
}

// Auto-initialize generic workflow if element exists
document.addEventListener('DOMContentLoaded', () => {
  createGenericWorkflow('ml-workflow-generic');
});
