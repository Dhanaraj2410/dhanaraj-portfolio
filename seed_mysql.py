#!/usr/bin/env python
"""
Seed script: populates MySQL dhanaraj_portfolio with all resume data.
Run from: portfolio/ directory
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import (
    SiteSettings, Profile, Education, Experience, Project,
    ProjectTechnology, Skill, Certification, SocialLink,
    JobRole, RoleResume, Activity, Achievement
)

print("=== Seeding MySQL database ===")

# ── SiteSettings ──────────────────────────────────────────────────────────────
s = SiteSettings.load()
s.site_title = "Dhanaraj Arjun Lokhande | AI/ML Engineer & Data Scientist"
s.tagline    = "AI/ML Engineer | Data Scientist | GenAI & RAG Specialist | Python Developer"
s.github_username = "Dhanaraj2410"
s.save()
print("✓ SiteSettings")

# ── Profile ───────────────────────────────────────────────────────────────────
p, _ = Profile.objects.get_or_create(id=1)
p.full_name = "Dhanaraj Arjun Lokhande"
p.title     = "AI/ML Engineer | Data Scientist | Python Developer"
p.location  = "Pune, Maharashtra, India"
p.email     = "lokhandedhanraj2410@gmail.com"
p.phone     = "+91 7507855698"
p.bio = (
    "Entry-level AI/ML Engineer and Data Scientist skilled in Python, SQL, Machine Learning, NLP, "
    "and Generative AI. Experienced in EDA, feature engineering, predictive modeling, and visualization "
    "using Pandas, NumPy, Scikit-learn, TensorFlow/Keras, and Power BI. Built AI applications using "
    "RAG, FAISS, Sentence Transformers, and the OpenAI API. Deployed ML solutions with Django and Docker."
)
p.professional_summary = p.bio
p.save()
print("✓ Profile")

# ── Social Links ──────────────────────────────────────────────────────────────
socials = [
    ('email',    'lokhandedhanraj2410@gmail.com',                           'Email',    1),
    ('github',   'https://github.com/Dhanaraj2410',                         'GitHub',   2),
    ('linkedin', 'https://www.linkedin.com/in/dhanaraj-lokhande2410',       'LinkedIn', 3),
    ('whatsapp', 'https://wa.me/917507855698',                              'WhatsApp', 4),
]
for platform, url, display, order in socials:
    obj, created = SocialLink.objects.get_or_create(platform=platform)
    obj.url = url; obj.display_name = display; obj.order = order
    obj.save()
print("✓ SocialLinks")

# ── Education ─────────────────────────────────────────────────────────────────
Education.objects.all().delete()
edu_data = [
    ('Bachelor of Engineering – Information Technology', 'BE',  'Savitribai Phule Pune University', 'SPPU', 2022, 2026, 8.54,  None, 1),
    ('Higher Secondary Certificate (HSC)',               'HSC', 'Dhanaji Nana Mahavidyalaya',        '',     2021, 2022, None,  75.0, 2),
    ('Secondary School Certificate (SSC)',               'SSC', 'G.G. Bendale High School',          '',     2019, 2020, None,  79.2, 3),
]
for degree, level, inst, uni, sy, ey, cgpa, pct, order in edu_data:
    Education.objects.create(
        degree=degree, level=level, institution=inst, university=uni,
        start_year=sy, end_year=ey, cgpa=cgpa, percentage=pct, order=order
    )
print("✓ Education")

# ── Experience ────────────────────────────────────────────────────────────────
Experience.objects.all().delete()
exp_data = [
    {
        'title': 'AI Trainee',
        'company': 'Plainsurf Solutions Pvt Ltd',
        'location': 'Pune, Maharashtra, India',
        'start_date': '2026-10-01',
        'end_date': None,
        'is_current': True,
        'responsibilities': (
            "• Working on AI/ML solutions using Python, NLP, and Generative AI techniques.\n"
            "• Applying machine learning, LLM, and RAG concepts to build and test AI-powered applications."
        ),
        'order': 1,
    },
    {
        'title': 'Data Science Intern',
        'company': 'Technoworld Softwares',
        'location': 'Pune, Maharashtra, India',
        'start_date': '2026-02-01',
        'end_date': '2026-07-31',
        'is_current': False,
        'responsibilities': (
            "• Performed data cleaning, EDA, and visualization using Python, Pandas, NumPy, and SQL.\n"
            "• Built and evaluated ML models using Scikit-learn.\n"
            "• Developed Power BI dashboards and Excel reports for KPI reporting."
        ),
        'order': 2,
    },
    {
        'title': 'Python Intern',
        'company': 'QSpiders',
        'location': 'Pune, Maharashtra, India',
        'start_date': '2026-01-01',
        'end_date': '2026-10-31',
        'is_current': False,
        'responsibilities': (
            "• Developed Django applications and REST APIs using Python, OOP, SQL/MySQL, and CRUD operations.\n"
            "• Debugged and tested applications to ensure reliable data flow and application stability."
        ),
        'order': 3,
    },
]
for e in exp_data:
    Experience.objects.create(**e)
print("✓ Experience")

# ── Projects ──────────────────────────────────────────────────────────────────
Project.objects.all().delete()
projects = [
    {
        'title': 'AI-Powered Document Intelligence & RAG Assistant',
        'slug':  'ai-powered-document-intelligence-rag-assistant',
        'short_description': 'RAG system for semantic search, PDF Q&A, and summarization using Python, Django, FAISS, Sentence Transformers, OpenAI API, and Docker.',
        'description': (
            'Engineered an enterprise-grade Document Intelligence and RAG system capable of ingesting PDF documents, '
            'generating dense vector embeddings with Sentence Transformers, and indexing with FAISS for sub-millisecond '
            'semantic retrieval. Integrated OpenAI API for LLM-powered Q&A, summarization, and multi-document comparison. '
            'REST APIs via DRF, PostgreSQL backend, containerized with Docker.'
        ),
        'problem_statement': 'Enterprise users spend hours reading lengthy PDFs to extract business-critical answers.',
        'solution': 'Semantic chunking + FAISS vector indexing + LLM synthesis for instant, cited PDF Q&A.',
        'algorithm': 'RAG (Retrieval-Augmented Generation), Sentence Transformers, FAISS HNSW index, OpenAI GPT',
        'results': 'Sub-500ms retrieval, 95%+ answer relevance, multi-document comparison support.',
        'github_url': 'https://github.com/Dhanaraj2410/AI-Powered-Document-IntelligenceRAG-Assistant',
        'live_demo_url': 'https://dhanaraj-portfolio-4az6.onrender.com',
        'is_featured': True,
        'order': 1,
        'techs': ['Python', 'Django', 'DRF', 'PostgreSQL', 'FAISS', 'Sentence Transformers', 'OpenAI API', 'Docker'],
    },
    {
        'title': 'Intelligent Loan Risk Assessment & Prediction Platform',
        'slug':  'intelligent-loan-risk-assessment-prediction-platform',
        'short_description': 'ML/DL loan risk system using XGBoost, Random Forest, Logistic Regression, and ANN with feature engineering and 86%+ accuracy.',
        'description': (
            'End-to-end Loan Risk Assessment Platform with XGBoost, Random Forest, Logistic Regression, and ANN. '
            'Automated preprocessing pipelines, cross-validation, hyperparameter tuning, model comparison benchmarks, '
            'financial calculations (EMI, DTI ratio), and historical prediction tracking with MySQL.'
        ),
        'algorithm': 'XGBoost, Random Forest, Logistic Regression, ANN (TensorFlow/Keras)',
        'results': '86%+ prediction accuracy, automated EMI & DTI calculations, full Django deployment.',
        'github_url': 'https://github.com/Dhanaraj2410/Intelligent-Loan-Risk-Assessment-Prediction-Platform',
        'is_featured': True,
        'order': 2,
        'techs': ['Python', 'Pandas', 'Scikit-learn', 'XGBoost', 'TensorFlow/Keras', 'MySQL', 'Django'],
    },
    {
        'title': 'AI-Powered Mock Interview Platform',
        'slug':  'ai-powered-mock-interview-platform',
        'short_description': 'AI interview platform with NLP resume analysis, dynamic question generation, real-time feedback, and OpenAI API integration.',
        'description': (
            'AI-based mock interview platform built with Python, Django, NLP, and the OpenAI API. Provides automated '
            'resume analysis, intelligent interview question generation, answer evaluation, and performance analytics. '
            'Full-stack with React frontend and Spring Boot microservice.'
        ),
        'algorithm': 'NLP (spaCy/NLTK), OpenAI GPT for question generation and answer scoring, cosine similarity',
        'results': 'Real-time interview scoring, resume–JD match scoring, skill gap identification.',
        'github_url': 'https://github.com/Dhanaraj2410/CareerAI-AI-Powered-Interview-Preparation-System',
        'is_featured': True,
        'order': 3,
        'techs': ['Python', 'NLP', 'Django', 'React', 'MySQL', 'OpenAI API', 'Spring Boot'],
    },
    {
        'title': 'InsurePredict – Insurance Cost Prediction',
        'slug':  'insurepredict-insurance-cost-prediction',
        'short_description': 'Linear Regression model predicting medical insurance costs from demographic data with EDA on 1300+ records.',
        'description': (
            'Machine learning pipeline using Linear Regression for predicting medical insurance premiums. '
            'Includes thorough EDA on 1,300+ healthcare records, feature engineering, Seaborn visualizations, '
            'and a Django-deployed prediction interface.'
        ),
        'algorithm': 'Linear Regression, EDA, Feature Engineering',
        'results': 'High accuracy linear model; EDA revealed key price drivers: smoking, BMI, region.',
        'github_url': 'https://github.com/Dhanaraj2410/InsurePredict-Insurance-Cost-Prediction-using-Linear-Regression',
        'is_featured': False,
        'order': 4,
        'techs': ['Python', 'Pandas', 'Seaborn', 'Scikit-learn', 'Django', 'SQL'],
    },
]
for proj_data in projects:
    techs = proj_data.pop('techs')
    proj = Project.objects.create(**proj_data)
    for t in techs:
        ProjectTechnology.objects.create(project=proj, name=t)
print("✓ Projects")

# ── Skills ────────────────────────────────────────────────────────────────────
Skill.objects.all().delete()
skills = [
    # Programming
    ('Python',               'PROGRAMMING', 92),
    ('SQL (MySQL)',           'PROGRAMMING', 88),
    ('Java (Basics)',         'PROGRAMMING', 60),
    ('R (Basics)',            'PROGRAMMING', 50),
    # ML / AI
    ('Machine Learning',     'ML_AI',       88),
    ('Deep Learning',        'ML_AI',       75),
    ('NLP',                  'ML_AI',       80),
    ('Generative AI / LLM',  'ML_AI',       78),
    ('RAG Systems',          'ML_AI',       80),
    ('Computer Vision',      'ML_AI',       60),
    # Frameworks / Libraries
    ('Scikit-learn',         'FRAMEWORK',   90),
    ('Pandas',               'FRAMEWORK',   92),
    ('NumPy',                'FRAMEWORK',   90),
    ('TensorFlow/Keras',     'FRAMEWORK',   72),
    ('Matplotlib/Seaborn',   'FRAMEWORK',   88),
    ('Django / DRF',         'FRAMEWORK',   85),
    ('FAISS',                'FRAMEWORK',   75),
    ('Sentence Transformers','FRAMEWORK',   75),
    ('OpenAI API',           'FRAMEWORK',   78),
    # Tools
    ('Power BI',             'TOOL',        82),
    ('Excel (Advanced)',     'TOOL',        80),
    ('Git / GitHub',         'TOOL',        85),
    ('Docker',               'TOOL',        65),
    ('Jupyter Notebook',     'TOOL',        92),
    ('MySQL Workbench',      'TOOL',        82),
    ('VS Code',              'TOOL',        90),
    ('Tableau (Basics)',     'TOOL',        60),
    # Databases
    ('MySQL',                'DATABASE',    88),
    ('PostgreSQL',           'DATABASE',    72),
    ('SQLite',               'DATABASE',    80),
    # Soft Skills
    ('Problem Solving',      'SOFT',        90),
    ('Communication',        'SOFT',        85),
    ('Team Collaboration',   'SOFT',        85),
    ('Fast Learner',         'SOFT',        90),
]
for name, cat, level in skills:
    Skill.objects.create(name=name, category=cat, proficiency=level)
print(f"✓ Skills ({len(skills)} entries)")

# ── Certifications ────────────────────────────────────────────────────────────
Certification.objects.all().delete()
certs = [
    ('Professional Certification in Data Science & Artificial Intelligence',
     'Indian Institute of Technology (IIT) Roorkee – iHUB DivyaSampark',
     'Data Science, Machine Learning, Deep Learning, AI, Hands-on Projects',
     'certificates/IIT_Roorkee_AI_20Bo6T2.jpg', 1),
    ('SQL Course Certification',
     'Intellipaat',
     'SQL Queries, Joins, Filtering, Stored Procedures, Database Design',
     'certificates/SQL_intellipaat_GHGSKGL.png', 2),
    ('Power BI Certification',
     'R3 Sys',
     'Dashboard Design, DAX, Business Intelligence, Data Modeling',
     'certificates/PowerBI_VndDlfN.jpeg', 3),
    ('AI Tools & ChatGPT Workshop',
     'be10x',
     'AI Tools, Prompt Engineering, Data Analysis, Automation',
     'certificates/be10x_Ai_tool_workshop_c6vyE9w.png', 4),
]
for title, org, skills_str, img, order in certs:
    Certification.objects.create(
        title=title, organization=org, skills=skills_str,
        certificate_image=img, order=order
    )
print("✓ Certifications")

# ── Job Roles ─────────────────────────────────────────────────────────────────
JobRole.objects.all().delete()
roles = [
    'Data Science', 'Machine Learning Engineer', 'AI Engineer',
    'Data Analyst', 'Python Developer', 'Business Analyst',
    'SQL Developer', 'NLP Engineer',
]
for i, role in enumerate(roles):
    JobRole.objects.create(title=role, order=i)
print("✓ JobRoles")

# ── Activities ────────────────────────────────────────────────────────────────
Activity.objects.all().delete()
acts = [
    ('GitHub Projects & Commits',    'CODING',    'Active GitHub development with 15+ Python & ML repositories.', '2024-01-01'),
    ('Kaggle Competitions',          'CODING',    'Participating in Kaggle ML competitions for practical skill-building.', '2025-01-01'),
    ('Open Source Contributions',    'CODING',    'Contributing to Python, Django, and ML open-source projects.', '2026-01-01'),
    ('AI & ML Online Courses',       'LEARNING',  'Continuously learning via Coursera, Udemy, and YouTube deep dives.', '2024-01-01'),
    ('Research Paper Reading',       'LEARNING',  'Reading and implementing ML/DL papers from ArXiv and PapersWithCode.', '2025-01-01'),
    ('Portfolio Building',           'LEARNING',  'Building production-grade AI portfolio projects with real datasets.', '2026-01-01'),
    ('LinkedIn Technical Writing',   'COMMUNITY', 'Sharing ML insights, project breakdowns, and learnings on LinkedIn.', '2026-01-01'),
]
for name, cat, desc, date in acts:
    Activity.objects.create(title=name, category=cat, description=desc, date=date)
print("✓ Activities")

# ── Verify ────────────────────────────────────────────────────────────────────
print("\n=== Seed Summary ===")
print(f"Profile:          {Profile.objects.count()}")
print(f"Experience:       {Experience.objects.count()}")
print(f"Education:        {Education.objects.count()}")
print(f"Projects:         {Project.objects.count()}")
print(f"Skills:           {Skill.objects.count()}")
print(f"Certifications:   {Certification.objects.count()}")
print(f"Social Links:     {SocialLink.objects.count()}")
print(f"Activities:       {Activity.objects.count()}")
print("=== Done! ===")
