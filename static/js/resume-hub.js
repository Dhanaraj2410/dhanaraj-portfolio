/* =============================================
   RESUME-HUB.JS — Multi-Role Resumes & Admin Upload Support
   Dhanaraj Arjun Lokhande — 2026 Fresher Candidate
   ============================================= */

// Candidate Master Profile for 2026 Fresher
const CANDIDATE_PROFILE = {
  name: "Dhanaraj Arjun Lokhande",
  graduationYear: 2026,
  status: "2026 Fresh Graduate (B.E. Information Technology)",
  university: "Savitribai Phule Pune University (SPPU)",
  cgpa: "8.54",
  location: "Pune, Maharashtra, India",
  email: "lokhandedhanraj2410@gmail.com",
  phone: "+91 7507855698",
  linkedin: "https://www.linkedin.com/in/dhanaraj-lokhande2410",
  github: "https://github.com/Dhanaraj2410",
  certifications: [
    "IIT Roorkee (iHUB DivyaSampark) — Data Science & AI Professional Certification",
    "Intellipaat — SQL Course Certification",
    "R3 Sys — Power BI Certification",
    "be10x — AI Tools & ChatGPT Workshop"
  ],
  internships: [
    {
      role: "AI Trainee",
      company: "Plainsurf Solutions Pvt Ltd, Pune",
      period: "Oct 2026 — Present",
      bullets: [
        "Working on AI/ML and Generative AI solutions using Python, NLP, LLMs, and the OpenAI API.",
        "Building and testing RAG-based and ML-driven features with embeddings and vector search for semantic retrieval."
      ]
    },
    {
      role: "Data Science Intern",
      company: "Technoworld Softwares, Pune",
      period: "Feb 2026 — Jul 2026",
      bullets: [
        "Building end-to-end ML models and data preprocessing pipelines using Python and Scikit-learn.",
        "Performing exploratory data analysis (EDA), feature selection, and model evaluation on production datasets.",
        "Collaborating with cross-functional teams to integrate predictive models into web interfaces."
      ]
    },
    {
      role: "Python Intern",
      company: "QSpiders, Pune",
      period: "Jan 2026 — Sep 2026",
      bullets: [
        "Developed Django applications and REST APIs using Python, OOP, SQL/MySQL, and CRUD operations.",
        "Debugged and tested applications to ensure reliable data flow and application stability."
      ]
    }
  ]
};

// Role-specific resume data tailored for 2026 Fresher applications
const ROLE_RESUMES = {
  "general": {
    id: "general",
    roleTitle: "General AI/ML Resume",
    badge: "📄 Complete Professional Profile",
    summary: "Information Technology graduate with an 8.54 CGPA and hands-on experience in Python, SQL, machine learning, NLP, Generative AI, RAG, Django, dashboards, databases, and backend development.",
    topSkills: ["Python", "SQL", "Django / DRF", "Machine Learning", "NLP", "Generative AI", "RAG / FAISS", "Power BI", "Docker"],
    keyProjects: [
      { title: "AI-Powered Document Intelligence & RAG Assistant", tech: "Python, Django, FAISS, Sentence Transformers, OpenAI API", points: ["Built a document Q&A and semantic search system using retrieval-augmented generation."] },
      { title: "Intelligent Loan Risk Assessment & Prediction Platform", tech: "Python, Scikit-learn, XGBoost, Django", points: ["Developed an ML risk prediction platform with feature engineering and model evaluation."] }
    ],
    adminResumeUrl: null
  },

  "data-analyst": {
    id: "data-analyst",
    roleTitle: "Data Analyst / Business Analyst",
    badge: "📊 Analytics & BI Focus",
    summary: "Data Analyst with hands-on experience in SQL, Python, Power BI, Excel, Tableau, and Business Intelligence. Skilled in data cleaning, EDA, ETL, data modeling, dashboard development, KPI reporting, and data visualization.",
    topSkills: ["SQL / MySQL / PostgreSQL", "Python / Pandas / NumPy", "Power BI / DAX", "Power Query / ETL", "Excel / Pivot Tables", "Tableau", "EDA & Data Cleaning", "Data Modeling", "KPI Reporting"],
    keyProjects: [
      {
        title: "InsurePredict — Exploratory Data Analysis & Cost Pipeline",
        tech: "Python, Pandas, Seaborn, SQL, Power BI",
        points: [
          "Executed thorough EDA on 1,300+ healthcare records to uncover demographic price drivers.",
          "Designed clear visualizations and charts highlighting risk factors and premium variance."
        ]
      },
      {
        title: "AI Loan Risk & Customer Demographics Dashboard",
        tech: "Power BI, SQL, Excel, Python",
        points: [
          "Developed executive dashboards summarizing loan approval distributions across urban & rural areas.",
          "Automated KPI calculation pipeline improving decision turnaround time."
        ]
      }
    ],
    adminResumeUrl: null
  },

  "data-science": {
    id: "data-science",
    roleTitle: "Data Scientist / Data Science",
    badge: "🤖 Predictive Analytics & Modeling",
    summary: "Entry-level AI/ML Engineer and Data Scientist skilled in Python, SQL, machine learning, NLP, and Generative AI. Experienced in data cleaning, EDA, feature engineering, predictive modeling, visualization, RAG, FAISS, Django, and Docker.",
    topSkills: ["Python / SQL", "Pandas / NumPy", "EDA & Data Cleaning", "Feature Engineering", "Regression / Classification", "XGBoost / Scikit-learn", "TensorFlow / Keras", "NLP / RAG", "Power BI"],
    keyProjects: [
      {
        title: "InsurePredict — Health Insurance Premium Prediction Engine",
        tech: "Python, Scikit-learn, Linear Regression, Django",
        points: [
          "Built a high-accuracy regression model trained on 1,300+ patient demographic records.",
          "Implemented automated feature scaling, encoding, and cross-validation for maximum model stability."
        ]
      },
      {
        title: "Intelligent Loan Risk Assessment & Prediction Platform",
        tech: "Python, Scikit-learn, Random Forest/Logistic Regression, MySQL",
        points: [
          "Achieved 86% accuracy in predicting applicant loan eligibility based on financial attributes.",
          "Engineered risk probability scoring system to assist automated decision-making."
        ]
      }
    ],
    adminResumeUrl: null
  },

  "machine-learning": {
    id: "machine-learning",
    roleTitle: "Machine Learning / AI Engineer",
    badge: "🧠 AI / ML & GenAI Systems",
    summary: "Entry-level AI/ML Engineer with hands-on experience building machine learning, deep learning, NLP, and Generative AI applications in Python. Built RAG pipelines and deployed ML/DL models as Django REST APIs.",
    topSkills: ["Regression / Classification", "Random Forest / XGBoost", "Scikit-learn", "TensorFlow / Keras", "NLP / LLMs", "Generative AI / RAG", "FAISS / Embeddings", "Django / DRF", "Model Evaluation"],
    keyProjects: [
      {
        title: "AI-Powered Mock Interview & Scoring Platform",
        tech: "Python, NLP, OpenAI API, Django, React, MySQL",
        points: [
          "Engineered an NLP system that parses candidate resumes and generates contextual interview questions.",
          "Integrated Generative AI feedback loop providing real-time answer scoring and actionable advice."
        ]
      },
      {
        title: "Real-Time ML Loan Risk Prediction API",
        tech: "Python, Scikit-learn, Django REST, JavaScript",
        points: [
          "Deployed an interactive ML decision engine with 86% accuracy and instant real-time risk assessment.",
          "Created interactive sliders for live parameter tuning and instant visual inference."
        ]
      }
    ],
    adminResumeUrl: null
  },

  "python-developer": {
    id: "python-developer",
    roleTitle: "Python Developer / Backend Engineer",
    badge: "🐍 Core Python & Web Development",
    summary: "Entry-level Python Developer with hands-on experience in Python, Django, Django REST Framework, REST APIs, SQL, MySQL, PostgreSQL, OOP, AI/ML integration, debugging, and SDLC practices.",
    topSkills: ["Core Python / OOP", "Django / DRF", "REST APIs", "SQL / MySQL / PostgreSQL", "JavaScript / HTML5 / CSS3", "Pandas / NumPy", "Git / GitHub", "Docker", "DSA / Debugging"],
    keyProjects: [
      {
        title: "AI Mock Interview Web Platform (Django & REST)",
        tech: "Python, Django, Spring Boot, MySQL, REST API",
        points: [
          "Developed full-stack web endpoints using Django and REST architecture for interview workflows.",
          "Designed database models, views, and authentication pipelines with MySQL persistence."
        ]
      },
      {
        title: "InsurePredict Web Application",
        tech: "Python, Django, Scikit-learn, HTML/CSS, JavaScript",
        points: [
          "Architected clean Django MVC structure connecting trained ML models to web forms.",
          "Optimized backend request handling for sub-100ms response times."
        ]
      }
    ],
    adminResumeUrl: null
  },

  "sql-developer": {
    id: "sql-developer",
    roleTitle: "SQL Developer / Database Analyst",
    badge: "🗃️ Database Engineering & Queries",
    summary: "Entry-level SQL Developer and Data Analyst with hands-on experience in SQL, MySQL, PostgreSQL, joins, CTEs, subqueries, window functions, ETL, KPI reporting, Power BI, Excel, and data validation.",
    topSkills: ["Advanced SQL", "MySQL / PostgreSQL", "Joins / CTEs / Subqueries", "Window Functions", "Data Cleaning & Validation", "ETL / Data Modeling", "Power BI / DAX", "Excel / KPI Reporting", "Python / Pandas"],
    keyProjects: [
      {
        title: "Relational Database Engine for Financial Loan Systems",
        tech: "MySQL, SQL, Database Schema Design, ER Modeling",
        points: [
          "Designed 3NF normalized relational schema for managing applicant records, loan terms, and credit scores.",
          "Wrote complex multi-table JOIN queries and subqueries to calculate real-time approval rates."
        ]
      },
      {
        title: "Healthcare Insurance Analytics Database",
        tech: "MySQL, SQL Queries, Power BI, Python",
        points: [
          "Created optimized database views and indexes reducing query execution times by 40%.",
          "Connected MySQL database with Power BI and Python for automated reporting."
        ]
      }
    ],
    adminResumeUrl: null
  }
};

document.addEventListener('DOMContentLoaded', () => {

  /* ---------- Check for Admin Uploaded Resumes in DOM ---------- */
  const djangoAdminResumes = document.querySelectorAll('[data-admin-resume]');
  djangoAdminResumes.forEach(el => {
    const role = el.dataset.role;
    const fileUrl = el.dataset.adminResume;
    if (ROLE_RESUMES[role] && fileUrl) {
      ROLE_RESUMES[role].adminResumeUrl = fileUrl;
    }
  });

  /* ---------- Role Tab Selection & Content Display ---------- */
  const roleButtons = document.querySelectorAll('.resume-role-tab');
  const roleDisplayContainer = document.getElementById('role-resume-display');
  const dataScienceTab = document.querySelector('.resume-role-tab[data-role="data-science"]');
  if (dataScienceTab) dataScienceTab.innerHTML = '<span>🤖</span> Data Scientist / Data Science';

  function renderRoleCard(roleKey) {
    const roleData = ROLE_RESUMES[roleKey];
    if (!roleData || !roleDisplayContainer) return;

    const hasAdminUpload = Boolean(roleData.adminResumeUrl);
    const downloadBtnHTML = hasAdminUpload
      ? `<a href="${roleData.adminResumeUrl}" target="_blank" download class="btn btn--primary btn--sm">
           <span>📥</span> Download Official Resume (PDF)
         </a>`
      : `<button class="btn btn--primary btn--sm" onclick="downloadRoleResume('${roleKey}')">
           <span>📥</span> Download PDF Resume
         </button>`;

    const badgeHTML = hasAdminUpload
      ? `<span class="resume-role-card__badge" style="background: rgba(16, 185, 129, 0.15); color: #059669; border: 1px solid rgba(16, 185, 129, 0.3);">
           ✅ Official Admin Resume Available
         </span>`
      : `<span class="resume-role-card__badge">${roleData.badge}</span>`;

    roleDisplayContainer.innerHTML = `
      <div class="resume-role-card reveal visible">
        <div class="resume-role-card__header">
          <div>
            ${badgeHTML}
            <h3 class="resume-role-card__title">${roleData.roleTitle}</h3>
            <p class="resume-role-card__subtitle">
              ${hasAdminUpload ? 'Official Admin-Uploaded Resume Ready for Download' : 'Tailored Profile for 2026 Fresh Graduate Applications'}
            </p>
          </div>
          <div class="resume-role-card__actions">
            ${downloadBtnHTML}
            <button class="btn btn--outline btn--sm" onclick="openResumePreviewModal('${roleKey}')">
              <span>👁️</span> Preview Resume
            </button>
          </div>
        </div>

        <div class="resume-role-card__body">
          <div class="resume-block">
            <h4 class="resume-block__title">🎯 Target Profile Summary</h4>
            <p class="resume-block__text">${roleData.summary}</p>
          </div>

          <div class="resume-block">
            <h4 class="resume-block__title">⚡ Core Technical Competencies</h4>
            <div class="resume-skills-tags">
              ${roleData.topSkills.map(skill => `<span class="skill-tag skill-tag--highlight">${skill}</span>`).join('')}
            </div>
          </div>

          <div class="resume-block">
            <h4 class="resume-block__title">🚀 Targeted Project Highlights</h4>
            <div class="role-projects-grid">
              ${roleData.keyProjects.map(proj => `
                <div class="role-project-card">
                  <div class="role-project-card__title">${proj.title}</div>
                  <div class="role-project-card__tech">Tech: ${proj.tech}</div>
                  <ul class="role-project-card__bullets">
                    ${proj.points.map(pt => `<li>${pt}</li>`).join('')}
                  </ul>
                </div>
              `).join('')}
            </div>
          </div>

          <div class="fresher-verification-banner">
            <div class="fresher-banner__icon">🎓</div>
            <div>
              <strong>Current Working Profile:</strong> AI Trainee at Plainsurf Solutions | B.E. IT Graduate (SPPU - 8.54 CGPA) | IIT Roorkee Certified.
            </div>
          </div>
        </div>
      </div>
    `;
  }

  roleButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      roleButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const roleKey = btn.dataset.role;
      renderRoleCard(roleKey);
    });
  });

  if (roleButtons.length > 0) {
    renderRoleCard('general');
  }


  /* ---------- Resume Modal Logic ---------- */
  const modal = document.getElementById('resume-modal');
  const modalBody = document.getElementById('resume-modal-body');
  const modalCloseBtn = document.getElementById('resume-modal-close');

  window.openResumePreviewModal = function(roleKey) {
    const roleData = ROLE_RESUMES[roleKey] || ROLE_RESUMES['data-analyst'];
    if (!modal || !modalBody) return;

    // Use the uploaded PDF for official resumes so the preview matches the
    // original black-and-white document exactly. Generated HTML remains the
    // fallback for roles without an uploaded PDF.
    if (roleData.adminResumeUrl) {
      const pdfUrl = `${roleData.adminResumeUrl}#toolbar=1&navpanes=0&scrollbar=1&view=FitH`;
      modalBody.innerHTML = `
        <div class="resume-pdf-viewer">
          <iframe class="resume-pdf-frame" src="${pdfUrl}" title="${roleData.roleTitle} resume preview"></iframe>
        </div>
      `;
    } else {
      modalBody.innerHTML = generatePrintableResumeHTML(roleData);
    }
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  window.closeResumeModal = function() {
    if (modal) {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }
  };

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', window.closeResumeModal);
  }
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) window.closeResumeModal();
    });
  }


  /* ---------- Dynamic PDF / HTML Resume Download Fallback ---------- */
  window.downloadRoleResume = function(roleKey) {
    const roleData = ROLE_RESUMES[roleKey] || ROLE_RESUMES['data-analyst'];
    
    if (roleData.adminResumeUrl) {
      const a = document.createElement('a');
      a.href = roleData.adminResumeUrl;
      a.download = `Dhanaraj_Lokhande_Official_${roleKey.toUpperCase()}_Resume`;
      a.target = "_blank";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      if (window.showToast) {
        showToast(`📥 Official Admin ${roleData.roleTitle} Resume downloading!`);
      }
      return;
    }

    const resumeHTML = generatePrintableResumeHTML(roleData, true);
    const printWindow = window.open('', '_blank');
    
    if (printWindow) {
      printWindow.document.write(resumeHTML);
      printWindow.document.close();
      printWindow.focus();
      setTimeout(() => {
        printWindow.print();
      }, 500);
      if (window.showToast) {
        showToast(`📄 Download window opened for Dhanaraj's ${roleData.roleTitle} Resume!`);
      }
    }
  };

});


/* ---------- Helper: HTML Resume Template Generator ---------- */
function generatePrintableResumeHTML(roleData, isStandalone = false) {
  const p = CANDIDATE_PROFILE;

  const styleTag = `
    <style>
      ${isStandalone ? "body { font-family: 'Segoe UI', Arial, sans-serif; color: #1e293b; line-height: 1.5; margin: 0; padding: 2rem; background: #fff; }" : ''}
      .res-container { max-width: 800px; margin: 0 auto; padding: 2rem; color: var(--text-primary, #1e293b); background: var(--bg-secondary, #fff); border: 1px solid var(--border-subtle, #e2e8f0); border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
      .res-header { text-align: center; border-bottom: 2px solid #6366f1; padding-bottom: 1rem; margin-bottom: 1.5rem; }
      .res-name { font-size: 2rem; font-weight: 800; color: var(--text-primary, #0f172a); margin: 0; letter-spacing: -0.5px; }
      .res-target { font-size: 1.1rem; font-weight: 700; color: var(--text-accent, #6366f1); margin-top: 0.25rem; text-transform: uppercase; letter-spacing: 0.5px; }
      .res-contact { font-size: 0.9rem; color: var(--text-secondary, #64748b); margin-top: 0.5rem; display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; }
      .res-contact a { color: #4338ca; text-decoration: none; }
      .res-section { margin-bottom: 1.5rem; }
      .res-sec-title { font-size: 1.1rem; font-weight: 700; color: var(--text-primary, #0f172a); border-bottom: 1.5px solid var(--border-color, #cbd5e1); padding-bottom: 0.25rem; margin-bottom: 0.75rem; text-transform: uppercase; }
      .res-summary { font-size: 0.95rem; color: var(--text-secondary, #334155); line-height: 1.6; }
      .res-skills-list { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem; }
      .res-skill-pill { background: var(--bg-input, #f1f5f9); color: var(--text-primary, #1e293b); padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.85rem; font-weight: 600; border: 1px solid var(--border-subtle, #e2e8f0); }
      .res-item { margin-bottom: 1rem; }
      .res-item-header { display: flex; justify-content: space-between; align-items: baseline; font-weight: 700; font-size: 0.95rem; color: var(--text-primary, #0f172a); }
      .res-item-sub { font-size: 0.85rem; color: var(--text-accent, #6366f1); font-weight: 600; margin-bottom: 0.3rem; }
      .res-bullets { margin: 0.3rem 0 0 1.2rem; padding: 0; font-size: 0.9rem; color: var(--text-secondary, #334155); }
      .res-bullets li { margin-bottom: 0.25rem; }
      .res-badge-2026 { background: #e0e7ff; color: #3730a3; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 700; font-size: 0.8rem; display: inline-block; margin-bottom: 0.5rem; }
      @media print {
        body { padding: 0; }
        .res-container { border: none; box-shadow: none; padding: 0; }
        .no-print { display: none !important; }
      }
    </style>
  `;

  const content = `
    <div class="res-container">
      <div class="res-header">
        <h1 class="res-name">${p.name}</h1>
        <div class="res-target">${roleData.roleTitle}</div>
        <span class="res-badge-2026">🎓 2026 FRESH GRADUATE (B.E. IT — 8.54 CGPA)</span>
        <div class="res-contact">
          <span>📍 ${p.location}</span>
          <span>📧 <a href="mailto:${p.email}">${p.email}</a></span>
          <span>📱 ${p.phone}</span>
          <span>💼 <a href="${p.linkedin}" target="_blank">LinkedIn</a></span>
          <span>🐙 <a href="${p.github}" target="_blank">GitHub</a></span>
        </div>
      </div>

      <div class="res-section">
        <div class="res-sec-title">Executive Summary</div>
        <p class="res-summary">${roleData.summary}</p>
      </div>

      <div class="res-section">
        <div class="res-sec-title">Core Technical Skills</div>
        <div class="res-skills-list">
          ${roleData.topSkills.map(s => `<span class="res-skill-pill">${s}</span>`).join('')}
        </div>
      </div>

      <div class="res-section">
        <div class="res-sec-title">Professional Experience</div>
        ${p.internships.map(intern => `
          <div class="res-item">
            <div class="res-item-header">
              <span>${intern.role} — ${intern.company}</span>
              <span>${intern.period}</span>
            </div>
            <ul class="res-bullets">
              ${intern.bullets.map(b => `<li>${b}</li>`).join('')}
            </ul>
          </div>
        `).join('')}
      </div>

      <div class="res-section">
        <div class="res-sec-title">Featured Projects</div>
        ${roleData.keyProjects.map(proj => `
          <div class="res-item">
            <div class="res-item-header">
              <span>${proj.title}</span>
            </div>
            <div class="res-item-sub">Technologies: ${proj.tech}</div>
            <ul class="res-bullets">
              ${proj.points.map(pt => `<li>${pt}</li>`).join('')}
            </ul>
          </div>
        `).join('')}
      </div>

      <div class="res-section">
        <div class="res-sec-title">Education</div>
        <div class="res-item">
          <div class="res-item-header">
            <span>B.E. Information Technology — ${p.university}</span>
            <span>2022 — 2026</span>
          </div>
          <div class="res-item-sub">Academic CGPA: <strong>${p.cgpa} / 10</strong> | Status: 2026 Graduating Batch</div>
        </div>
      </div>

      <div class="res-section">
        <div class="res-sec-title">Certifications & Credentials</div>
        <ul class="res-bullets">
          ${p.certifications.map(cert => `<li>${cert}</li>`).join('')}
        </ul>
      </div>

      ${isStandalone ? `
        <div class="no-print" style="margin-top: 2rem; text-align: center;">
          <button onclick="window.print()" style="background: #6366f1; color: white; padding: 0.6rem 1.5rem; border: none; border-radius: 6px; font-weight: 700; cursor: pointer;">
            🖨️ Print / Save as PDF
          </button>
        </div>
      ` : ''}
    </div>
  `;

  return isStandalone ? `<!DOCTYPE html><html><head><title>${p.name} - ${roleData.roleTitle} Resume</title>${styleTag}</head><body>${content}</body></html>` : (styleTag + content);
}

/* ---------- Certification Modal Viewer ---------- */
const CERT_DETAILS = {
  iit: {
    title: "Professional Certification in Data Science & AI",
    org: "IIT Roorkee (iHUB DivyaSampark)",
    date: "Issued 2026",
    badge: "🎓 Premium University Credential",
    desc: "Advanced professional training covering Supervised & Unsupervised Machine Learning algorithms, Deep Learning neural networks, Feature Engineering, Exploratory Data Analysis, and AI System Architecture.",
    skills: ["Machine Learning", "Deep Learning", "Python", "Data Science", "Model Architecture"]
  },
  sql: {
    title: "SQL Course Certification",
    org: "Intellipaat",
    date: "Issued 2025",
    badge: "🗃️ Database Engineering",
    desc: "Mastery in writing complex relational SQL queries, multi-table JOINs, subqueries, database schema design, indexing, stored procedures, and MySQL Workbench administration.",
    skills: ["SQL", "MySQL", "Schema Design", "Query Optimization", "Joins & Subqueries"]
  },
  powerbi: {
    title: "Power BI Certification",
    org: "R3 Sys",
    date: "Issued 2025",
    badge: "📊 Business Intelligence",
    desc: "Data modeling, interactive dashboard development, DAX expressions, ETL data cleaning, and business analytics visualization.",
    skills: ["Power BI", "DAX", "Data Modeling", "Business Intelligence", "Dashboards"]
  },
  ai: {
    title: "AI Tools & ChatGPT Workshop Certification",
    org: "be10x",
    date: "Issued 2025",
    badge: "🤖 Generative AI & Automation",
    desc: "Practical application of AI productivity tools, prompt engineering, generative AI workflows, and automated analytical pipelines.",
    skills: ["Generative AI", "ChatGPT", "AI Automation", "Prompt Engineering"]
  }
};

window.openCertModal = function(certKey) {
  const cert = CERT_DETAILS[certKey] || CERT_DETAILS['iit'];
  const modal = document.getElementById('resume-modal');
  const modalBody = document.getElementById('resume-modal-body');
  if (!modal || !modalBody) return;

  modalBody.innerHTML = `
    <div style="padding: 2.5rem; color: #1e293b;">
      <div style="text-align: center; border-bottom: 2px solid #6366f1; padding-bottom: 1.5rem; margin-bottom: 1.5rem;">
        <span style="font-size: 3rem; display: block; margin-bottom: 0.5rem;">🏆</span>
        <span style="background: #e0e7ff; color: #3730a3; padding: 0.3rem 0.8rem; border-radius: 999px; font-weight: 700; font-size: 0.8rem;">
          ${cert.badge}
        </span>
        <h2 style="font-size: 1.75rem; font-weight: 800; color: #0f172a; margin: 0.75rem 0 0.25rem;">${cert.title}</h2>
        <p style="font-size: 1.1rem; font-weight: 700; color: #6366f1; margin: 0;">Issued by ${cert.org} · ${cert.date}</p>
      </div>

      <div style="margin-bottom: 1.5rem;">
        <h4 style="font-size: 1rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem;">📜 Credential Overview</h4>
        <p style="font-size: 0.95rem; color: #334155; line-height: 1.6;">${cert.desc}</p>
      </div>

      <div style="margin-bottom: 1.5rem;">
        <h4 style="font-size: 1rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem;">⚡ Skills & Concepts Verified</h4>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
          ${cert.skills.map(s => `<span style="background: #f1f5f9; color: #1e293b; border: 1px solid #cbd5e1; padding: 0.3rem 0.8rem; border-radius: 6px; font-weight: 600; font-size: 0.85rem;">${s}</span>`).join('')}
        </div>
      </div>

      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; font-size: 0.85rem; color: #475569; display: flex; align-items: center; justify-content: space-between;">
        <span>Candidate: <strong>Dhanaraj Arjun Lokhande</strong> (2026 BE IT — 8.54 CGPA)</span>
        <span style="color: #059669; font-weight: 700;">✅ Verified Credential</span>
      </div>
    </div>
  `;

  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
};

/* ---------- Photo Modal Lightbox Viewer ---------- */
window.openPhotoModal = function(photoUrl, fullName) {
  const modal = document.getElementById('resume-modal');
  const modalBody = document.getElementById('resume-modal-body');
  if (!modal || !modalBody) return;

  const name = fullName || 'Dhanaraj Arjun Lokhande';
  const imgUrl = photoUrl && photoUrl.trim() !== '' 
    ? photoUrl 
    : 'https://ui-avatars.com/api/?name=Dhanaraj+Lokhande&size=512&background=6366f1&color=fff';

  modalBody.innerHTML = `
    <div style="text-align: center; padding: 2rem; color: #1e293b;">
      <h3 style="font-size: 1.25rem; font-weight: 800; color: #0f172a; margin-bottom: 0.25rem;">${name}</h3>
      <p style="font-size: 0.85rem; color: #6366f1; font-weight: 700; margin-bottom: 1.25rem;">2026 Fresh Graduate (B.E. IT — 8.54 CGPA at SPPU)</p>
      <div style="max-width: 440px; margin: 0 auto; border-radius: 16px; overflow: hidden; box-shadow: 0 12px 36px rgba(0,0,0,0.15); border: 2px solid #e2e8f0; background: #0f172a;">
        <img src="${imgUrl}" alt="${name}" style="width: 100%; max-height: 480px; object-fit: contain; display: block; margin: 0 auto;">
      </div>
      <div style="margin-top: 1.25rem; display: flex; justify-content: center; gap: 0.75rem;">
        <a href="${imgUrl}" target="_blank" download class="btn btn--primary btn--sm" style="padding: 0.5rem 1.2rem; background: #6366f1; color: white; border-radius: 6px; font-weight: 700; text-decoration: none; display: inline-block;">
          📥 Download Full Photo
        </a>
      </div>
    </div>
  `;

  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
};
