"""Static portfolio content - no database required (auto-generated)."""
from types import SimpleNamespace


class _All(list):
    def all(self):
        return self


class _File:
    def __init__(self, url=""):
        self._url = url or ""

    @property
    def url(self):
        return self._url

    def __bool__(self):
        return bool(self._url)

    def __str__(self):
        return self._url


class SocialLink(SimpleNamespace):
    def get_platform_display(self):
        return self.platform_display


SITE = SimpleNamespace(
    site_title='Dhanaraj Arjun Lokhande | AI/ML Engineer & Data Scientist',
    tagline='AI/ML Engineer | Data Scientist | GenAI & RAG Specialist | Python Developer',
    secondary_tagline='My Skills, Projects, Experience, Certifications & Career Journey — All in One Place.',
    github_username='Dhanaraj2410',
    linkedin_url='',
    meta_description='Dhanaraj Arjun Lokhande — AI/ML Engineer & Data Scientist portfolio showcasing Python, Machine Learning, and Data Science projects.',
)

PROFILE = SimpleNamespace(
    full_name='Dhanaraj Arjun Lokhande',
    title='AI/ML Engineer | Data Scientist | Python Developer',
    bio='Entry-level AI/ML Engineer and Data Scientist skilled in Python, SQL, Machine Learning, NLP, and Generative AI. Experienced in EDA, feature engineering, predictive modeling, and visualization using Pandas, NumPy, Scikit-learn, TensorFlow/Keras, and Power BI. Built AI applications using RAG, FAISS, Sentence Transformers, and the OpenAI API. Deployed ML solutions with Django and Docker.',
    location='Pune, Maharashtra, India',
    email='lokhandedhanraj2410@gmail.com',
    phone='+91 7507855698',
    professional_summary='Entry-level AI/ML Engineer and Data Scientist skilled in Python, SQL, Machine Learning, NLP, and Generative AI. Experienced in EDA, feature engineering, predictive modeling, and visualization using Pandas, NumPy, Scikit-learn, TensorFlow/Keras, and Power BI. Built AI applications using RAG, FAISS, Sentence Transformers, and the OpenAI API. Deployed ML solutions with Django and Docker.',
    photo=_File('/static/media/profile/photo.jpeg'),
    resume_pdf=_File('/static/media/resumes/roles/Dhanaraj_Resume_ML.pdf'),
)

EDUCATION = [
    SimpleNamespace(degree='Bachelor of Engineering – Information Technology', level='BE', institution='Savitribai Phule Pune University', university='SPPU', start_year=2022, end_year=2026, cgpa='8.54', percentage='', description='', score_display='CGPA: 8.54', order=1),
    SimpleNamespace(degree='Higher Secondary Certificate (HSC)', level='HSC', institution='Dhanaji Nana Mahavidyalaya', university='', start_year=2021, end_year=2022, cgpa='', percentage='75.00', description='', score_display='75.00%', order=2),
    SimpleNamespace(degree='Secondary School Certificate (SSC)', level='SSC', institution='G.G. Bendale High School', university='', start_year=2019, end_year=2020, cgpa='', percentage='79.20', description='', score_display='79.20%', order=3),
]

EXPERIENCE = [
    SimpleNamespace(title='AI Trainee', company='Plainsurf Solutions Pvt Ltd', location='Pune, Maharashtra, India', start_date='2026-10-01', end_date='', is_current=True, description='', responsibilities='• Working on AI/ML solutions using Python, NLP, and Generative AI techniques.\n• Applying machine learning, LLM, and RAG concepts to build and test AI-powered applications.', responsibilities_list=['• Working on AI/ML solutions using Python, NLP, and Generative AI techniques.', '• Applying machine learning, LLM, and RAG concepts to build and test AI-powered applications.'], duration_display='10/2026 - Present', order=1),
    SimpleNamespace(title='Data Science Intern', company='Technoworld Softwares', location='Pune, Maharashtra, India', start_date='2026-02-01', end_date='2026-07-31', is_current=False, description='', responsibilities='• Performed data cleaning, EDA, and visualization using Python, Pandas, NumPy, and SQL.\n• Built and evaluated ML models using Scikit-learn.\n• Developed Power BI dashboards and Excel reports for KPI reporting.', responsibilities_list=['• Performed data cleaning, EDA, and visualization using Python, Pandas, NumPy, and SQL.', '• Built and evaluated ML models using Scikit-learn.', '• Developed Power BI dashboards and Excel reports for KPI reporting.'], duration_display='02/2026 - 07/2026', order=2),
    SimpleNamespace(title='Python Intern', company='QSpiders', location='Pune, Maharashtra, India', start_date='2026-01-01', end_date='2026-10-31', is_current=False, description='', responsibilities='• Developed Django applications and REST APIs using Python, OOP, SQL/MySQL, and CRUD operations.\n• Debugged and tested applications to ensure reliable data flow and application stability.', responsibilities_list=['• Developed Django applications and REST APIs using Python, OOP, SQL/MySQL, and CRUD operations.', '• Debugged and tested applications to ensure reliable data flow and application stability.'], duration_display='01/2026 - 10/2026', order=3),
]

PROJECTS = [
    SimpleNamespace(
        title='AI-Powered Document Intelligence & RAG Assistant',
        slug='ai-powered-document-intelligence-rag-assistant',
        short_description='RAG system for semantic search, PDF Q&A, and summarization using Python, Django, FAISS, Sentence Transformers, OpenAI API, and Docker.',
        description='Engineered an enterprise-grade Document Intelligence and RAG system capable of ingesting PDF documents, generating dense vector embeddings with Sentence Transformers, and indexing with FAISS for sub-millisecond semantic retrieval. Integrated OpenAI API for LLM-powered Q&A, summarization, and multi-document comparison. REST APIs via DRF, PostgreSQL backend, containerized with Docker.',
        problem_statement='Enterprise users spend hours reading lengthy PDFs to extract business-critical answers.',
        solution='Semantic chunking + FAISS vector indexing + LLM synthesis for instant, cited PDF Q&A.',
        architecture='',
        features='',
        features_list=[],
        algorithm='RAG (Retrieval-Augmented Generation), Sentence Transformers, FAISS HNSW index, OpenAI GPT',
        dataset_info='',
        results='Sub-500ms retrieval, 95%+ answer relevance, multi-document comparison support.',
        challenges='',
        future_improvements='',
        github_url='https://github.com/Dhanaraj2410/AI-Powered-Document-IntelligenceRAG-Assistant',
        live_demo_url='https://dhanaraj-portfolio-4az6.onrender.com',
        screenshot=_File(''),
        is_featured=True,
        order=1,
        technologies=_All([SimpleNamespace(name='Python'), SimpleNamespace(name='Django'), SimpleNamespace(name='DRF'), SimpleNamespace(name='PostgreSQL'), SimpleNamespace(name='FAISS'), SimpleNamespace(name='Sentence Transformers'), SimpleNamespace(name='OpenAI API'), SimpleNamespace(name='Docker')]),
        workflow_steps=_All([]),
    ),
    SimpleNamespace(
        title='Intelligent Loan Risk Assessment & Prediction Platform',
        slug='intelligent-loan-risk-assessment-prediction-platform',
        short_description='ML/DL loan risk system using XGBoost, Random Forest, Logistic Regression, and ANN with feature engineering and 86%+ accuracy.',
        description='End-to-end Loan Risk Assessment Platform with XGBoost, Random Forest, Logistic Regression, and ANN. Automated preprocessing pipelines, cross-validation, hyperparameter tuning, model comparison benchmarks, financial calculations (EMI, DTI ratio), and historical prediction tracking with MySQL.',
        problem_statement='',
        solution='',
        architecture='',
        features='',
        features_list=[],
        algorithm='XGBoost, Random Forest, Logistic Regression, ANN (TensorFlow/Keras)',
        dataset_info='',
        results='86%+ prediction accuracy, automated EMI & DTI calculations, full Django deployment.',
        challenges='',
        future_improvements='',
        github_url='https://github.com/Dhanaraj2410/Intelligent-Loan-Risk-Assessment-Prediction-Platform',
        live_demo_url='',
        screenshot=_File(''),
        is_featured=True,
        order=2,
        technologies=_All([SimpleNamespace(name='Python'), SimpleNamespace(name='Pandas'), SimpleNamespace(name='Scikit-learn'), SimpleNamespace(name='XGBoost'), SimpleNamespace(name='TensorFlow/Keras'), SimpleNamespace(name='MySQL'), SimpleNamespace(name='Django')]),
        workflow_steps=_All([]),
    ),
    SimpleNamespace(
        title='AI-Powered Mock Interview Platform',
        slug='ai-powered-mock-interview-platform',
        short_description='AI interview platform with NLP resume analysis, dynamic question generation, real-time feedback, and OpenAI API integration.',
        description='AI-based mock interview platform built with Python, Django, NLP, and the OpenAI API. Provides automated resume analysis, intelligent interview question generation, answer evaluation, and performance analytics. Full-stack with React frontend and Spring Boot microservice.',
        problem_statement='',
        solution='',
        architecture='',
        features='',
        features_list=[],
        algorithm='NLP (spaCy/NLTK), OpenAI GPT for question generation and answer scoring, cosine similarity',
        dataset_info='',
        results='Real-time interview scoring, resume–JD match scoring, skill gap identification.',
        challenges='',
        future_improvements='',
        github_url='https://github.com/Dhanaraj2410/CareerAI-AI-Powered-Interview-Preparation-System',
        live_demo_url='',
        screenshot=_File(''),
        is_featured=True,
        order=3,
        technologies=_All([SimpleNamespace(name='Python'), SimpleNamespace(name='NLP'), SimpleNamespace(name='Django'), SimpleNamespace(name='React'), SimpleNamespace(name='MySQL'), SimpleNamespace(name='OpenAI API'), SimpleNamespace(name='Spring Boot')]),
        workflow_steps=_All([]),
    ),
    SimpleNamespace(
        title='InsurePredict – Insurance Cost Prediction',
        slug='insurepredict-insurance-cost-prediction',
        short_description='Linear Regression model predicting medical insurance costs from demographic data with EDA on 1300+ records.',
        description='Machine learning pipeline using Linear Regression for predicting medical insurance premiums. Includes thorough EDA on 1,300+ healthcare records, feature engineering, Seaborn visualizations, and a Django-deployed prediction interface.',
        problem_statement='',
        solution='',
        architecture='',
        features='',
        features_list=[],
        algorithm='Linear Regression, EDA, Feature Engineering',
        dataset_info='',
        results='High accuracy linear model; EDA revealed key price drivers: smoking, BMI, region.',
        challenges='',
        future_improvements='',
        github_url='https://github.com/Dhanaraj2410/InsurePredict-Insurance-Cost-Prediction-using-Linear-Regression',
        live_demo_url='',
        screenshot=_File(''),
        is_featured=False,
        order=4,
        technologies=_All([SimpleNamespace(name='Python'), SimpleNamespace(name='Pandas'), SimpleNamespace(name='Seaborn'), SimpleNamespace(name='Scikit-learn'), SimpleNamespace(name='Django'), SimpleNamespace(name='SQL')]),
        workflow_steps=_All([]),
    ),
]

SKILLS = [
    SimpleNamespace(name='Python', category='PROGRAMMING', category_display='Programming', proficiency=92, icon='', order=0),
    SimpleNamespace(name='Pandas', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=92, icon='', order=0),
    SimpleNamespace(name='Jupyter Notebook', category='TOOL', category_display='TOOL', proficiency=92, icon='', order=0),
    SimpleNamespace(name='NumPy', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=90, icon='', order=0),
    SimpleNamespace(name='Fast Learner', category='SOFT', category_display='Soft Skills', proficiency=90, icon='', order=0),
    SimpleNamespace(name='VS Code', category='TOOL', category_display='TOOL', proficiency=90, icon='', order=0),
    SimpleNamespace(name='Problem Solving', category='SOFT', category_display='Soft Skills', proficiency=90, icon='', order=0),
    SimpleNamespace(name='Scikit-learn', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=90, icon='', order=0),
    SimpleNamespace(name='SQL (MySQL)', category='PROGRAMMING', category_display='Programming', proficiency=88, icon='', order=0),
    SimpleNamespace(name='Machine Learning', category='ML_AI', category_display='ML_AI', proficiency=88, icon='', order=0),
    SimpleNamespace(name='Matplotlib/Seaborn', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=88, icon='', order=0),
    SimpleNamespace(name='MySQL', category='DATABASE', category_display='DATABASE', proficiency=88, icon='', order=0),
    SimpleNamespace(name='Django / DRF', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=85, icon='', order=0),
    SimpleNamespace(name='Git / GitHub', category='TOOL', category_display='TOOL', proficiency=85, icon='', order=0),
    SimpleNamespace(name='Communication', category='SOFT', category_display='Soft Skills', proficiency=85, icon='', order=0),
    SimpleNamespace(name='Team Collaboration', category='SOFT', category_display='Soft Skills', proficiency=85, icon='', order=0),
    SimpleNamespace(name='MySQL Workbench', category='TOOL', category_display='TOOL', proficiency=82, icon='', order=0),
    SimpleNamespace(name='Power BI', category='TOOL', category_display='TOOL', proficiency=82, icon='', order=0),
    SimpleNamespace(name='NLP', category='ML_AI', category_display='ML_AI', proficiency=80, icon='', order=0),
    SimpleNamespace(name='RAG Systems', category='ML_AI', category_display='ML_AI', proficiency=80, icon='', order=0),
    SimpleNamespace(name='Excel (Advanced)', category='TOOL', category_display='TOOL', proficiency=80, icon='', order=0),
    SimpleNamespace(name='SQLite', category='DATABASE', category_display='DATABASE', proficiency=80, icon='', order=0),
    SimpleNamespace(name='Generative AI / LLM', category='ML_AI', category_display='ML_AI', proficiency=78, icon='', order=0),
    SimpleNamespace(name='OpenAI API', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=78, icon='', order=0),
    SimpleNamespace(name='Deep Learning', category='ML_AI', category_display='ML_AI', proficiency=75, icon='', order=0),
    SimpleNamespace(name='FAISS', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=75, icon='', order=0),
    SimpleNamespace(name='Sentence Transformers', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=75, icon='', order=0),
    SimpleNamespace(name='TensorFlow/Keras', category='FRAMEWORK', category_display='FRAMEWORK', proficiency=72, icon='', order=0),
    SimpleNamespace(name='PostgreSQL', category='DATABASE', category_display='DATABASE', proficiency=72, icon='', order=0),
    SimpleNamespace(name='Docker', category='TOOL', category_display='TOOL', proficiency=65, icon='', order=0),
    SimpleNamespace(name='Java (Basics)', category='PROGRAMMING', category_display='Programming', proficiency=60, icon='', order=0),
    SimpleNamespace(name='Computer Vision', category='ML_AI', category_display='ML_AI', proficiency=60, icon='', order=0),
    SimpleNamespace(name='Tableau (Basics)', category='TOOL', category_display='TOOL', proficiency=60, icon='', order=0),
    SimpleNamespace(name='R (Basics)', category='PROGRAMMING', category_display='Programming', proficiency=50, icon='', order=0),
]

CERTIFICATIONS = [
    SimpleNamespace(title='Professional Certification in Data Science & Artificial Intelligence', organization='Indian Institute of Technology (IIT) Roorkee – iHUB DivyaSampark', description='', skills='Data Science, Machine Learning, Deep Learning, AI, Hands-on Projects', skills_list=['Data Science, Machine Learning, Deep Learning, AI, Hands-on Projects'], certificate_image=_File('/static/media/certificates/IIT_Roorkee_AI_20Bo6T2.jpg'), certificate_pdf=_File(''), verification_url='', date_earned='', order=1),
    SimpleNamespace(title='SQL Course Certification', organization='Intellipaat', description='', skills='SQL Queries, Joins, Filtering, Stored Procedures, Database Design', skills_list=['SQL Queries, Joins, Filtering, Stored Procedures, Database Design'], certificate_image=_File('/static/media/certificates/SQL_intellipaat_GHGSKGL.png'), certificate_pdf=_File(''), verification_url='', date_earned='', order=2),
    SimpleNamespace(title='Power BI Certification', organization='R3 Sys', description='', skills='Dashboard Design, DAX, Business Intelligence, Data Modeling', skills_list=['Dashboard Design, DAX, Business Intelligence, Data Modeling'], certificate_image=_File('/static/media/certificates/PowerBI_VndDlfN.jpeg'), certificate_pdf=_File(''), verification_url='', date_earned='', order=3),
    SimpleNamespace(title='AI Tools & ChatGPT Workshop', organization='be10x', description='', skills='AI Tools, Prompt Engineering, Data Analysis, Automation', skills_list=['AI Tools, Prompt Engineering, Data Analysis, Automation'], certificate_image=_File('/static/media/certificates/be10x_Ai_tool_workshop_c6vyE9w.png'), certificate_pdf=_File(''), verification_url='', date_earned='', order=4),
]

ACTIVITIES = [
    SimpleNamespace(title='Open Source Contributions', category='CODING', category_display='Coding Activity', description='Contributing to Python, Django, and ML open-source projects.', date='2026-01-01', icon='📌', order=0),
    SimpleNamespace(title='Portfolio Building', category='LEARNING', category_display='Learning Activity', description='Building production-grade AI portfolio projects with real datasets.', date='2026-01-01', icon='📌', order=0),
    SimpleNamespace(title='LinkedIn Technical Writing', category='COMMUNITY', category_display='COMMUNITY', description='Sharing ML insights, project breakdowns, and learnings on LinkedIn.', date='2026-01-01', icon='📌', order=0),
    SimpleNamespace(title='Kaggle Competitions', category='CODING', category_display='Coding Activity', description='Participating in Kaggle ML competitions for practical skill-building.', date='2025-01-01', icon='📌', order=0),
    SimpleNamespace(title='Research Paper Reading', category='LEARNING', category_display='Learning Activity', description='Reading and implementing ML/DL papers from ArXiv and PapersWithCode.', date='2025-01-01', icon='📌', order=0),
    SimpleNamespace(title='GitHub Projects & Commits', category='CODING', category_display='Coding Activity', description='Active GitHub development with 15+ Python & ML repositories.', date='2024-01-01', icon='📌', order=0),
    SimpleNamespace(title='AI & ML Online Courses', category='LEARNING', category_display='Learning Activity', description='Continuously learning via Coursera, Udemy, and YouTube deep dives.', date='2024-01-01', icon='📌', order=0),
]

ACHIEVEMENTS = [
]

SOCIAL_LINKS = [
    SocialLink(platform='email', platform_display='Email', url='lokhandedhanraj2410@gmail.com', display_name='Email', icon_class='', order=1),
    SocialLink(platform='github', platform_display='GitHub', url='https://github.com/Dhanaraj2410', display_name='GitHub', icon_class='', order=2),
    SocialLink(platform='linkedin', platform_display='LinkedIn', url='https://www.linkedin.com/in/dhanaraj-lokhande2410', display_name='LinkedIn', icon_class='', order=3),
    SocialLink(platform='whatsapp', platform_display='whatsapp', url='https://wa.me/917507855698', display_name='WhatsApp', icon_class='', order=4),
]

JOB_ROLES = [
    SimpleNamespace(title='Data Science', order=0),
    SimpleNamespace(title='Machine Learning Engineer', order=1),
    SimpleNamespace(title='AI Engineer', order=2),
    SimpleNamespace(title='Data Analyst', order=3),
    SimpleNamespace(title='Python Developer', order=4),
    SimpleNamespace(title='Business Analyst', order=5),
    SimpleNamespace(title='SQL Developer', order=6),
    SimpleNamespace(title='NLP Engineer', order=7),
]

ROLE_RESUMES = [
    SimpleNamespace(role_key='data-analyst', title='Data Analyst / Business Analyst', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Dhanaraj_Resume_Data_Analyst.pdf'), order=1),
    SimpleNamespace(role_key='machine-learning', title='Machine Learning / AI Engineer', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Dhanaraj_Resume_ML.pdf'), order=2),
    SimpleNamespace(role_key='python-developer', title='Python Developer', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Dhanaraj_Resume_Python_Developer.pdf'), order=3),
]
