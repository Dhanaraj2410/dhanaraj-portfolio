/* ═══════════════════════════════════════════════════════════════════════════
   Ask Dhanaraj AI — 100% Reliable Recruiter Assistant Chatbot
   ═══════════════════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
  initChatbot();
});

function initChatbot() {
  const toggle = document.getElementById('chatbot-toggle');
  const window_ = document.getElementById('chatbot-window');
  const close = document.getElementById('chatbot-close');
  const input = document.getElementById('chatbot-input');
  const sendBtn = document.getElementById('chatbot-send');
  const messages = document.getElementById('chatbot-messages');

  if (!toggle || !window_) return;

  // Toggle chat window
  toggle.addEventListener('click', () => {
    window_.classList.toggle('active');
    if (window_.classList.contains('active')) {
      input.focus();
    }
  });

  close.addEventListener('click', () => {
    window_.classList.remove('active');
  });

  // Send message on click or Enter key
  sendBtn.addEventListener('click', () => sendMessage());
  input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
  });

  // Predefined Question Chips Click Event
  document.querySelectorAll('.chat-suggestion').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const questionText = btn.textContent.trim();
      input.value = questionText;
      sendMessage();
    });
  });

  // Initial Welcome message
  addMessage('ai', "👋 Hi! I'm **Ask Dhanaraj AI** — your AI Recruiter Assistant. Click any predefined question below or ask me about Dhanaraj's background!");

  function sendMessage() {
    const msg = input.value.trim();
    if (!msg) return;

    // Render User Message
    addMessage('user', msg);
    input.value = '';

    // Show Typing Indicator
    const typingEl = showTyping();

    // Generate AI response with slight delay for realistic conversation feel
    setTimeout(() => {
      removeTyping(typingEl);
      const reply = generateRecruiterAIReply(msg);
      addMessage('ai', reply);
    }, 350);
  }

  function addMessage(type, text) {
    const div = document.createElement('div');
    div.className = `chat-message ${type}`;
    const formatted = text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\n/g, '<br>');
    div.innerHTML = formatted;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function showTyping() {
    const div = document.createElement('div');
    div.className = 'chat-typing';
    div.innerHTML = '<span></span><span></span><span></span>';
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
    return div;
  }

  function removeTyping(el) {
    if (el && el.parentNode) {
      el.parentNode.removeChild(el);
    }
  }
}


/* ═══════════════════════════════════════════════════════════════════════════
   Recruiter Questions Response Engine (100% Offline & Instant)
   ═══════════════════════════════════════════════════════════════════════════ */
function generateRecruiterAIReply(userMsg) {
  const msg = userMsg.toLowerCase().trim();

  // 1. What skills does Dhanaraj have?
  if (msg.includes('skill') || msg.includes('technolog') || msg.includes('stack') || msg.includes('know') || msg.includes('tool')) {
    return `⚡ **Technical Skills & Stack — Dhanaraj Arjun Lokhande:**\n\n` +
      `🐍 **Programming Languages:** Python 3 (Advanced OOP), SQL (MySQL), JavaScript, HTML5/CSS3\n` +
      `🤖 **Machine Learning & AI:** Scikit-learn, TensorFlow, Keras, NLP (Natural Language Processing), OpenAI API, GenAI, Feature Engineering, Regression & Classification\n` +
      `📊 **Data Analysis & BI:** Pandas, NumPy, Matplotlib, Seaborn, Power BI, Excel Charts, EDA\n` +
      `🏗️ **Frameworks & Dev Tools:** Django, RESTful APIs, MySQL Workbench, Git & GitHub, Jupyter Notebook, Google Colab\n\n` +
      `🎓 **Academic Foundation:** B.E. IT 2026 Batch from SPPU with **8.54 CGPA**.`;
  }

  // 2. What Machine Learning projects has he built?
  if (msg.includes('machine learning project') || msg.includes('ml project') || msg.includes('built') || msg.includes('machine learning')) {
    return `🤖 **Machine Learning Projects Built by Dhanaraj:**\n\n` +
      `1. **InsurePredict — Health Insurance Cost Prediction Engine**\n` +
      `   • Stack: Python, Scikit-learn, Linear Regression, Django, SQL, EDA\n` +
      `   • Executed EDA & feature engineering on 1,300+ patient records to deliver an accurate health premium estimator.\n\n` +
      `2. **AI-Powered Loan Approval Prediction & Risk System**\n` +
      `   • Stack: Python, Scikit-learn (Logistic Regression / Random Forest), Django, MySQL\n` +
      `   • Achieved **86% prediction accuracy** with a real-time risk assessment engine for applicant eligibility.\n\n` +
      `3. **AI-Powered Mock Interview Platform**\n` +
      `   • Stack: Python, NLP, OpenAI API, Django, React, MySQL\n` +
      `   • Built resume parsing & automated interview Q&A scoring algorithms.\n\n` +
      `🧪 *Try live interactive simulations in the ML Playground section on the site!*`;
  }

  // 3. What Python projects has he completed?
  if (msg.includes('python project') || msg.includes('django project') || msg.includes('completed') || msg.includes('python')) {
    return `🐍 **Python & Full-Stack Projects Completed:**\n\n` +
      `1. **AI Mock Interview Platform** — Django, OpenAI API, REST APIs, MySQL, NLP\n` +
      `2. **InsurePredict Web Application** — Django MVC, Scikit-learn, Linear Regression, HTML/CSS/JS\n` +
      `3. **AI Loan Approval Prediction System** — Django Backend, MySQL, ML Pipeline\n` +
      `4. **Developer Portfolio & AI Assistant Platform** — Custom Python/Django backend engine\n\n` +
      `💼 Dhanaraj also currently works as a **Python Developer Intern at QSpiders Pune**, writing modular OOP code and optimizing MySQL backend queries.`;
  }

  // 4. What internships does he have?
  if (msg.includes('internship') || msg.includes('work experience') || msg.includes('experience') || msg.includes('company') || msg.includes('qspiders') || msg.includes('technoworld')) {
    return `💼 **Practical Industry Internships (Currently Active):**\n\n` +
      `1. 🟢 **Data Science Intern — Technoworld Softwares, Pune** *(Feb 2026 — Present)*\n` +
      `   • Building production ML models, performing EDA, feature engineering, and model evaluation using Scikit-learn.\n\n` +
      `2. 🟢 **Python Developer Intern — QSpiders, Pune** *(Jan 2026 — Present)*\n` +
      `   • Developing modular OOP Python applications, writing complex SQL queries, and designing RESTful API logic.`;
  }

  // 5. What certifications does he have?
  if (msg.includes('certification') || msg.includes('certified') || msg.includes('course') || msg.includes('iit') || msg.includes('intellipaat') || msg.includes('power bi')) {
    return `📜 **Verified Professional Certifications & Credentials:**\n\n` +
      `1. 🎓 **IIT Roorkee (iHUB DivyaSampark)** — Professional Certification in Data Science & AI\n` +
      `2. 🗃️ **Intellipaat** — SQL Course Certification\n` +
      `3. 📊 **R3 Sys** — Power BI Certification\n` +
      `4. 🤖 **be10x** — AI Tools & ChatGPT Workshop Certification\n\n` +
      `🔍 *Click "View Certificate" in the Certifications section on the page to view credentials!*`;
  }

  // 6. Is he available for work?
  if (msg.includes('available') || msg.includes('availability') || msg.includes('join') || msg.includes('start') || msg.includes('notice')) {
    return `🟢 **Availability Status:**\n\n` +
      `Yes! Dhanaraj Arjun Lokhande is **Open to Work & Available Immediately** for full-time entry-level engineering roles.\n\n` +
      `• **Status:** 2026 Graduating Batch (BE IT, SPPU — 8.54 CGPA)\n` +
      `• **Work Preference:** In-office (Pune / Bangalore / PAN India), Hybrid, or Remote\n` +
      `• **Notice Period:** Immediate Joiner / 0 Days\n\n` +
      `📧 **Contact:** lokhandedhanraj2410@gmail.com | 📱 +91 7507855698`;
  }

  // 7. What roles is he looking for?
  if (msg.includes('role') || msg.includes('looking for') || msg.includes('position') || msg.includes('target') || msg.includes('job')) {
    return `🎯 **Target Positions & Roles:**\n\n` +
      `Dhanaraj is actively seeking entry-level / fresher positions in:\n\n` +
      `1. 🐍 **Python Developer**\n` +
      `2. 📊 **Data Analyst**\n` +
      `3. 🤖 **Data Scientist**\n` +
      `4. ⚙️ **Machine Learning Engineer**\n` +
      `5. 🧠 **AI/ML Engineer**\n` +
      `6. 🚀 **Junior AI Engineer**\n` +
      `7. 🔬 **Junior Data Scientist**\n` +
      `8. 💻 **Python/Django Developer**`;
  }

  // 8. Why should we hire him?
  if (msg.includes('why') || msg.includes('hire') || msg.includes('reasons') || msg.includes('strengths') || msg.includes('advantage')) {
    return `🌟 **Top 5 Reasons to Hire Dhanaraj Arjun Lokhande:**\n\n` +
      `1. 🎓 **Proven Academic Excellence:** 8.54 CGPA in B.E. Information Technology from SPPU.\n` +
      `2. 💼 **Dual Active Internships:** Gaining real industry experience in Data Science (Technoworld Softwares) and Python Dev (QSpiders).\n` +
      `3. 📜 **IIT Roorkee Certified:** Verified professional certification in Data Science & Artificial Intelligence.\n` +
      `4. 🚀 **End-to-End Build Capabilities:** Skilled in going from raw data to trained ML models and deployed Django web applications.\n` +
      `5. ⚡ **Fast Learner & Immediate Availability:** Ready to make an immediate impact from Day 1!`;
  }

  // Default Recruiter Response
  return `👋 Hi! I'm **Ask Dhanaraj AI**.\n\n` +
    `Click any predefined recruiter question above or ask me about:\n` +
    `• **Technical Stack (Python, SQL, ML, Power BI)**\n` +
    `• **Machine Learning & Python Projects**\n` +
    `• **Internships & Academics (8.54 CGPA)**\n` +
    `• **Certifications (IIT Roorkee)**\n` +
    `• **Target Roles & Availability**`;
}
