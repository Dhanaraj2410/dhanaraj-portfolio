# Dhanaraj AI/ML Portfolio & Career Showcase Platform

A production-grade, interactive full-stack portfolio platform for **Dhanaraj Arjun Lokhande** — AI/ML Engineer, Data Scientist, and Generative AI Developer. Built with Python, Django, Django REST Framework, MySQL / PostgreSQL, and a modern glassmorphic responsive UI.

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.1%2B-green.svg?logo=django&logoColor=white)](https://djangoproject.com)
[![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-orange.svg?logo=mysql&logoColor=white)](https://mysql.com)
[![Render](https://img.shields.io/badge/Render-Deployed-purple.svg?logo=render&logoColor=white)](https://dhanaraj-portfolio-4az6.onrender.com)
[![GitHub](https://img.shields.io/badge/GitHub-Dhanaraj2410-181717.svg?logo=github&logoColor=white)](https://github.com/Dhanaraj2410)

---

## 👨‍💻 Candidate Overview

- **Name**: Dhanaraj Arjun Lokhande
- **Target Roles**: AI/ML Engineer | Data Scientist | Generative AI & RAG Developer | Python Backend Developer
- **Education**: Bachelor of Engineering, Information Technology (2022–2026) — Savitribai Phule Pune University (SPPU) | **CGPA: 8.54**
- **Location**: Pune, Maharashtra, India
- **Email**: [lokhandedhanraj2410@gmail.com](mailto:lokhandedhanraj2410@gmail.com)
- **LinkedIn**: [linkedin.com/in/dhanaraj-lokhande2410](https://www.linkedin.com/in/dhanaraj-lokhande2410)
- **Live Portfolio**: [dhanaraj-portfolio-4az6.onrender.com](https://dhanaraj-portfolio-4az6.onrender.com)

---

## 🌟 Industry Experience

1. **AI Trainee** | Plainsurf Solutions Pvt Ltd, Pune *(10/2026 – Present)*
   - Developing AI/ML solutions using Python, NLP, and Generative AI (RAG) techniques.
   - Applying machine learning, LLM, and dense vector search concepts to build and test production AI applications.
2. **Data Science Intern** | Technoworld Softwares, Pune *(02/2026 – 07/2026)*
   - Performed data cleaning, EDA, and statistical visualization using Python, Pandas, NumPy, and SQL.
   - Trained and evaluated machine learning models with Scikit-learn; engineered Power BI dashboards and Excel reports for KPI tracking.
3. **Python Intern** | QSpiders, Pune *(01/2026 – 10/2026)*
   - Developed Django web applications and modular REST APIs using OOP, SQL/MySQL, and CRUD patterns.
   - Debugged and tested database transactions ensuring stable, high-throughput backend data flows.

---

## 🚀 Flagship Projects

| Project | Tech Stack | Highlights |
|---|---|---|
| **AI-Powered Document Intelligence & RAG Assistant** | Python, Django, DRF, PostgreSQL, FAISS, Sentence Transformers, OpenAI API, Docker | Enterprise RAG system for semantic search, multi-document summarization, PDF Q&A, and citation-grounded retrieval. |
| **Intelligent Loan Risk Assessment & Prediction Platform** | Python, Pandas, Scikit-learn, XGBoost, TensorFlow/Keras, MySQL, Django | Multi-model risk prediction (XGBoost, Random Forest, Logistic Regression, ANN) with 86%+ accuracy, EMI/DTI calculators, and prediction history. |
| **AI-Powered Mock Interview Platform** | Python, NLP, Django, React, MySQL, OpenAI API | Automated resume analysis, dynamic question generation, real-time candidate answer evaluation, and scoring feedback. |
| **InsurePredict – Insurance Cost Prediction** | Python, Scikit-learn, Django, SQL, EDA, Seaborn | Medical insurance premium estimation using Linear Regression on 1,300+ records with full demographic EDA pipeline. |

---

## 📜 Certifications

- **Professional Certification in Data Science & Artificial Intelligence** — IIT Roorkee, iHUB DivyaSampark
- **SQL Course Certification** — Intellipaat
- **Power BI Certification** — R3 Sys
- **AI Tools and ChatGPT Workshop** — be10x

---

## 🛠️ Architecture & Features

- **Multi-Database Support**: Seamless automatic switching between **MySQL** (via PyMySQL), **PostgreSQL** (via dj-database-url), and **SQLite** (for quick local development).
- **Dynamic Content Administration**: Every project, skill, internship, certification, and timeline entry is fully manageable via the Django Admin panel at `/admin/`.
- **RESTful API**: Clean REST API endpoints exposed via Django REST Framework at `/api/` with throttling and CORS headers.
- **Interactive Recruiter Tools**: Live skill match analysis, role-tailored resume generation, and interactive terminal interface.
- **Production-Ready Security**: WhiteNoise compressed static assets, CSRF protection, secure cookies, and automated superuser seeding.

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Dhanaraj2410/dhanaraj-portfolio.git
cd dhanaraj-portfolio/portfolio
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment (`.env`)
```bash
cp .env.example .env
```
To run with **MySQL**:
```env
DB_ENGINE=mysql
DB_NAME=dhanaraj_portfolio
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```
To run with **SQLite** (zero configuration):
```env
DB_ENGINE=sqlite
```

### 5. Initialize Database & Seed Resume Data
```bash
python manage.py migrate
python manage.py seed_data
```

### 6. Run Development Server
```bash
python manage.py runserver
```
Visit `http://localhost:8000` to explore the live portfolio!

---

## 📄 License
This project is open-source under the MIT License.
