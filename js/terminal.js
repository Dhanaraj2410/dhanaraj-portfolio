/* =============================================
   TERMINAL.JS — Interactive Developer Console
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {
  const terminalBody = document.getElementById('terminal-body');
  const terminalInput = document.getElementById('terminal-input');
  if (!terminalBody || !terminalInput) return;

  const PROMPT = 'visitor@portfolio:~$ ';

  // Command history
  let history = [];
  let historyIndex = -1;

  // Command definitions
  const commands = {

    help: () => [
      { text: '📖 Available Commands:', cls: 'info' },
      { text: '' },
      { text: '  about        — Who is Dhanaraj?' },
      { text: '  skills       — Technical proficiencies' },
      { text: '  projects     — Featured project list' },
      { text: '  experience   — Work experience' },
      { text: '  education    — Academic background' },
      { text: '  certs        — Certifications earned' },
      { text: '  contact      — Get in touch' },
      { text: '  social       — Social media links' },
      { text: '  whoami       — About you (the visitor)' },
      { text: '  date         — Current date & time' },
      { text: '  resume       — Download resume link' },
      { text: '  clear        — Clear terminal' },
      { text: '  help         — Show this help menu' },
      { text: '' },
      { text: '💡 Tip: Press ↑ ↓ to navigate command history', cls: 'highlight' },
    ],

    about: () => [
      { text: '👤 About Dhanaraj Lokhande', cls: 'info' },
      { text: '─────────────────────────────' },
      { text: '  Name:     Dhanaraj Arjun Lokhande' },
      { text: '  Title:    AI/ML Engineer & Data Scientist' },
      { text: '  Location: Pune, Maharashtra, India' },
      { text: '  CGPA:     8.54 (SPPU — B.E. IT)' },
      { text: '' },
      { text: '  Passionate about turning raw data into intelligent', cls: 'success' },
      { text: '  applications using ML, NLP, and full-stack dev.', cls: 'success' },
    ],

    skills: () => [
      { text: '⚡ Technical Skills', cls: 'info' },
      { text: '─────────────────────────────' },
      { text: '  Languages:    Python · SQL · JavaScript · Java' },
      { text: '  ML/AI:        Scikit-learn · TensorFlow · Keras · NLP' },
      { text: '  Libraries:    NumPy · Pandas · Matplotlib · Seaborn' },
      { text: '  Frameworks:   Django · React · Spring Boot · REST APIs' },
      { text: '  Visualization: Power BI · Tableau' },
      { text: '  Tools:        Git · VS Code · Jupyter · Google Colab' },
    ],

    projects: () => [
      { text: '🔨 Featured Projects', cls: 'info' },
      { text: '─────────────────────────────' },
      { text: '' },
      { text: '  [01] 🎙️ AI-Powered Mock Interview Platform', cls: 'highlight' },
      { text: '       Stack: Python, NLP, OpenAI, Django, React, MySQL' },
      { text: '       → NLP resume analysis + AI-generated interviews' },
      { text: '' },
      { text: '  [02] 🏥 InsurePredict — Insurance Cost Prediction', cls: 'highlight' },
      { text: '       Stack: Python, Scikit-learn, Django, SQL' },
      { text: '       → EDA + Linear Regression on 1300+ records' },
      { text: '' },
      { text: '  [03] 🏦 AI-Powered Loan Approval Prediction', cls: 'highlight' },
      { text: '       Stack: Python, Django, Scikit-learn, MySQL, JS' },
      { text: '       → 86% accuracy, real-time risk assessment' },
      { text: '' },
      { text: '  💡 Try the live ML demos → scroll to ML Playground!', cls: 'success' },
    ],

    experience: () => [
      { text: '💼 Work Experience', cls: 'info' },
      { text: '─────────────────────────────' },
      { text: '' },
      { text: '  🟢 Data Science Intern — Technoworld Softwares', cls: 'highlight' },
      { text: '     Feb 2026 – Present | Pune' },
      { text: '     ML models, EDA, feature engineering, Scikit-learn' },
      { text: '' },
      { text: '  🟢 Python Developer Intern — QSpiders', cls: 'highlight' },
      { text: '     Jan 2026 – Present | Pune' },
      { text: '     Python OOP, SQL integration, mini-projects' },
    ],

    education: () => [
      { text: '🎓 Education', cls: 'info' },
      { text: '─────────────────────────────' },
      { text: '  B.E. IT — SPPU (2022–2026)  CGPA: 8.54 ⭐', cls: 'highlight' },
      { text: '  HSC — D.N. Mahavidyalaya     Score: 75.00%' },
      { text: '  SSC — G.G. Bendale HS         Score: 79.20%' },
    ],

    certs: () => [
      { text: '🏆 Certifications', cls: 'info' },
      { text: '─────────────────────────────' },
      { text: '  🎓 IIT Roorkee — Data Science & AI (Professional)' },
      { text: '  🗃️ Intellipaat — SQL Course' },
      { text: '  📊 R3 Sys — Power BI' },
      { text: '  🤖 be10x — AI Tools & ChatGPT Workshop' },
    ],

    contact: () => [
      { text: '📬 Contact Information', cls: 'info' },
      { text: '─────────────────────────────' },
      { text: '  📧 lokhandedhanraj2410@gmail.com' },
      { text: '  📱 +91 7507855698' },
      { text: '  📍 Pune, Maharashtra, India' },
      { text: '' },
      { text: '  Feel free to reach out! 🤝', cls: 'success' },
    ],

    social: () => [
      { text: '🌐 Social Links', cls: 'info' },
      { text: '─────────────────────────────' },
      { text: '  LinkedIn: linkedin.com/in/dhanaraj-lokhande-a27536283' },
      { text: '  GitHub:   github.com/DhanarajLokhande' },
      { text: '  WhatsApp: wa.me/917507855698' },
    ],

    whoami: () => [
      { text: '🧑‍💻 You are a curious visitor exploring Dhanaraj\'s portfolio!', cls: 'success' },
      { text: '   Welcome! Feel free to explore using the commands above.' },
    ],

    date: () => {
      const now = new Date();
      return [
        { text: `📅 ${now.toLocaleDateString('en-IN', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}` },
        { text: `🕐 ${now.toLocaleTimeString('en-IN')}` },
      ];
    },

    resume: () => {
      const resumeSec = document.getElementById('resume');
      if (resumeSec) {
        setTimeout(() => {
          const top = resumeSec.getBoundingClientRect().top + window.scrollY - 80;
          window.scrollTo({ top, behavior: 'smooth' });
        }, 300);
      }
      return [
        { text: '📄 2026 Fresher Career & Multi-Role Resume Hub', cls: 'info' },
        { text: '─────────────────────────────────────────────' },
        { text: '  Tailored Resumes Available for 5 Key Roles:' },
        { text: '   1. 📊 Data Analyst / Business Analyst' },
        { text: '   2. 🤖 Data Science / Data Scientist' },
        { text: '   3. 🧠 Machine Learning / AI Engineer' },
        { text: '   4. 🐍 Python Developer' },
        { text: '   5. 🗃️ SQL Developer' },
        { text: '' },
        { text: '  🚀 Scrolling you straight to the Resume Hub & ATS Analyzer...', cls: 'success' },
      ];
    },

    clear: () => 'CLEAR',

    '': () => [],
  };

  // Aliases
  commands.hi = commands.hello = () => [
    { text: '👋 Hey there! Nice to meet you!', cls: 'success' },
    { text: '   Type "help" to see what I can tell you.', cls: '' },
  ];

  commands.ls = commands.dir = () => [
    { text: 'about.txt  skills.json  projects/  experience/  contact.md  README.md', cls: '' },
  ];

  commands.cat = () => [
    { text: '🐱 Meow! Did you mean a specific file? Try "about" or "skills".', cls: 'highlight' },
  ];

  commands.sudo = () => [
    { text: '🚫 Nice try! You don\'t have sudo access here 😄', cls: 'error' },
  ];

  commands.exit = commands.quit = () => [
    { text: '👋 Thanks for visiting! Refresh the page to start a new session.', cls: 'success' },
  ];


  /* ---------- Process Command ---------- */
  function processCommand(cmd) {
    const trimmed = cmd.trim().toLowerCase();
    const parts = trimmed.split(/\s+/);
    const mainCmd = parts[0];

    if (mainCmd === 'clear') {
      clearTerminal();
      return;
    }

    // Add command line to output
    addOutputLine(`${PROMPT}${cmd}`, 'command');

    if (commands[mainCmd]) {
      const output = commands[mainCmd]();
      if (Array.isArray(output)) {
        output.forEach(line => {
          addOutputLine(line.text, line.cls || '');
        });
      }
    } else if (trimmed.length > 0) {
      addOutputLine(`Command not found: "${mainCmd}". Type "help" for available commands.`, 'error');
    }

    // Add new input line
    addInputLine();
    scrollToBottom();
  }


  /* ---------- DOM Helpers ---------- */
  function addOutputLine(text, cls = '') {
    // Remove the current input line first
    const currentInputLine = terminalBody.querySelector('.terminal__input-line');
    if (currentInputLine) currentInputLine.remove();

    const line = document.createElement('div');
    line.className = 'terminal__line';

    if (cls === 'command') {
      line.innerHTML = `<span class="terminal__output">${escapeHTML(text)}</span>`;
    } else {
      const span = document.createElement('span');
      span.className = `terminal__output${cls ? ' terminal__output--' + cls : ''}`;
      span.textContent = text;
      line.appendChild(span);
    }

    terminalBody.appendChild(line);
  }

  function addInputLine() {
    const line = document.createElement('div');
    line.className = 'terminal__line terminal__input-line';
    line.innerHTML = `<span class="terminal__prompt">${PROMPT}</span>`;

    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'terminal__input';
    input.autocomplete = 'off';
    input.spellcheck = false;

    input.addEventListener('keydown', handleInput);
    line.appendChild(input);
    terminalBody.appendChild(line);
    input.focus();
  }

  function clearTerminal() {
    terminalBody.innerHTML = '';
    addOutputLine('Terminal cleared. Type "help" for commands.', 'info');
    addInputLine();
    scrollToBottom();
  }

  function scrollToBottom() {
    terminalBody.scrollTop = terminalBody.scrollHeight;
  }

  function escapeHTML(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }


  /* ---------- Input Handler ---------- */
  function handleInput(e) {
    if (e.key === 'Enter') {
      const cmd = e.target.value;
      if (cmd.trim()) {
        history.unshift(cmd);
        historyIndex = -1;
      }
      e.target.removeEventListener('keydown', handleInput);
      e.target.disabled = true;
      e.target.parentElement.classList.remove('terminal__input-line');
      processCommand(cmd);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (historyIndex < history.length - 1) {
        historyIndex++;
        e.target.value = history[historyIndex];
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex > 0) {
        historyIndex--;
        e.target.value = history[historyIndex];
      } else {
        historyIndex = -1;
        e.target.value = '';
      }
    }
  }


  /* ---------- Initial Setup ---------- */
  // Bind the initial input
  terminalInput.addEventListener('keydown', handleInput);

  // Click anywhere on terminal to focus input
  document.getElementById('terminal').addEventListener('click', () => {
    const activeInput = terminalBody.querySelector('.terminal__input-line .terminal__input');
    if (activeInput) activeInput.focus();
  });
});
