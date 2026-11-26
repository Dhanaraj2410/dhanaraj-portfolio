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
    tagline='Aspiring AI/ML Engineer | Data Scientist | Generative AI & RAG Developer | Data Analyst | Python Developer',
    secondary_tagline='My Skills, Projects, Experience, Certifications & Career Journey — All in One Place.',
    github_username='Dhanaraj2410',
    linkedin_url='',
    meta_description='Dhanaraj Arjun Lokhande — AI/ML Engineer & Data Scientist portfolio showcasing Python, Machine Learning, and Data Science projects.',
)

PROFILE = SimpleNamespace(
    full_name='Dhanaraj Arjun Lokhande',
    title='Aspiring AI/ML Engineer | Data Scientist | Generative AI & RAG Developer | Data Analyst | Python Developer',
    bio='Entry-level AI/ML Engineer and Data Scientist skilled in Python, SQL, Machine Learning, NLP, and Generative AI. Experienced in EDA, feature engineering, predictive modeling, and visualization using Pandas, NumPy, Scikit-learn, TensorFlow/Keras, and Power BI. Built AI applications using RAG, FAISS, Sentence Transformers, and the OpenAI API. Deployed ML solutions with Django and Docker.',
    location='Pune, Maharashtra, India',
    email='lokhandedhanraj2410@gmail.com',
    phone='+91 7507855698',
    professional_summary='Entry-level AI/ML Engineer and Data Scientist skilled in Python, SQL, Machine Learning, NLP, and Generative AI. Experienced in EDA, feature engineering, predictive modeling, and visualization using Pandas, NumPy, Scikit-learn, TensorFlow/Keras, and Power BI. Built AI applications using RAG, FAISS, Sentence Transformers, and the OpenAI API. Deployed ML solutions with Django and Docker.',
    photo=_File('/static/media/profile/photo.jpeg'),
    resume_pdf=_File('/static/media/resumes/roles/Resume(AI_ML).pdf'),
)

EDUCATION = [
    SimpleNamespace(degree='Bachelor of Engineering – Information Technology', level='BE', institution='Savitribai Phule Pune University', university='SPPU', start_year=2022, end_year=2026, cgpa='8.54', percentage='', description='', score_display='CGPA: 8.54', order=1),
    SimpleNamespace(degree='Higher Secondary Certificate (HSC)', level='HSC', institution='Dhanaji Nana Mahavidyalaya', university='', start_year=2021, end_year=2022, cgpa='', percentage='75.00', description='', score_display='75.00%', order=2),
    SimpleNamespace(degree='Secondary School Certificate (SSC)', level='SSC', institution='G.G. Bendale High School', university='', start_year=2019, end_year=2020, cgpa='', percentage='79.20', description='', score_display='79.20%', order=3),
]

EXPERIENCE = [
    SimpleNamespace(title='AI Trainee', company='Plainsurf Solutions Pvt Ltd', location='Pune, Maharashtra, India', start_date='2026-10-01', end_date='', is_current=True, description='', responsibilities='• Working on AI/ML and Generative AI solutions using Python, NLP, LLMs, and the OpenAI API.\n• Building and testing RAG-based and ML-driven features with embeddings and vector search for semantic retrieval.', responsibilities_list=['• Working on AI/ML and Generative AI solutions using Python, NLP, LLMs, and the OpenAI API.', '• Building and testing RAG-based and ML-driven features with embeddings and vector search for semantic retrieval.'], duration_display='10/2026 - Present', order=1),
    SimpleNamespace(title='Data Science Intern', company='Technoworld Softwares', location='Pune, Maharashtra, India', start_date='2026-02-01', end_date='2026-07-31', is_current=False, description='', responsibilities='• Built and evaluated machine learning models using Scikit-learn, including data preprocessing and feature engineering.\n• Cleaned and analysed datasets with Python, Pandas, NumPy, and SQL to prepare model-ready data.', responsibilities_list=['• Built and evaluated machine learning models using Scikit-learn, including data preprocessing and feature engineering.', '• Cleaned and analysed datasets with Python, Pandas, NumPy, and SQL to prepare model-ready data.'], duration_display='02/2026 - 07/2026', order=2),
    SimpleNamespace(title='Python Intern', company='QSpiders', location='Pune, Maharashtra, India', start_date='2026-01-01', end_date='2026-09-30', is_current=False, description='', responsibilities='• Developed Django applications and REST APIs using Python, OOP, SQL/MySQL, and CRUD operations.\n• Debugged and tested applications to ensure reliable data flow and application stability.', responsibilities_list=['• Developed Django applications and REST APIs using Python, OOP, SQL/MySQL, and CRUD operations.', '• Debugged and tested applications to ensure reliable data flow and application stability.'], duration_display='01/2026 - 09/2026', order=3),
]

PROJECTS = [
    SimpleNamespace(
        title='AI-Powered Document Intelligence & RAG Assistant',
        slug='ai-powered-document-intelligence-rag-assistant',
        short_description='RAG system for semantic search, PDF Q&A, and summarization using Python, Django, FAISS, Sentence Transformers, OpenAI API, and Docker.',
        description='Engineered an enterprise-grade Document Intelligence and RAG system capable of ingesting PDF documents, generating dense vector embeddings with Sentence Transformers, and indexing with FAISS for sub-millisecond semantic retrieval. Integrated OpenAI API for LLM-powered Q&A, summarization, and multi-document comparison. REST APIs via DRF, PostgreSQL backend, containerized with Docker.',
        problem_statement='Enterprise users spend hours reading lengthy PDFs to extract business-critical answers.',
        solution='Semantic chunking + FAISS vector indexing + LLM synthesis for instant, cited PDF Q&A.',
        architecture='Django + Django REST Framework API layer; PostgreSQL metadata store; Sentence Transformers embedding service; FAISS vector index; OpenAI generation layer; Docker deployment.',
        features='PDF upload and text extraction; semantic chunking; cited document Q&A; multi-document comparison; summarization; REST API access.',
        features_list=['Upload and index PDF documents', 'Semantic search with FAISS vector retrieval', 'Grounded Q&A with cited source context', 'Summarize and compare multiple documents', 'REST APIs with Docker-ready deployment'],
        algorithm='RAG (Retrieval-Augmented Generation), Sentence Transformers, FAISS HNSW index, OpenAI GPT',
        dataset_info='User-provided PDF documents are processed at ingestion time. The pipeline stores document metadata and embeddings for each uploaded file instead of relying on a fixed public dataset.',
        results='Sub-500ms retrieval, 95%+ answer relevance, multi-document comparison support.',
        challenges='Maintaining answer grounding across long documents, selecting useful chunk sizes, and keeping retrieval latency low while preserving relevant context.',
        future_improvements='Add streaming responses, OCR for scanned PDFs, access controls, evaluation datasets, and observability for retrieval and generation quality.',
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
        problem_statement='Loan approval decisions require consistent risk signals from applicant, financial, and demographic data while reducing manual assessment effort.',
        solution='A supervised learning pipeline compares multiple classifiers, applies preprocessing and feature engineering, and exposes the selected model through a Django application with financial calculators.',
        architecture='Django web application; Pandas preprocessing pipeline; Scikit-learn and XGBoost model layer; TensorFlow/Keras ANN benchmark; MySQL persistence for users and prediction history.',
        features='Model comparison and cross-validation; automated preprocessing; EMI and DTI calculations; risk prediction; historical prediction tracking.',
        features_list=['Compare Logistic Regression, Random Forest, XGBoost, and ANN models', 'Validate models with cross-validation and tuned hyperparameters', 'Calculate EMI and debt-to-income ratio', 'Store prediction history in MySQL', 'Serve predictions through a Django interface'],
        algorithm='XGBoost, Random Forest, Logistic Regression, ANN (TensorFlow/Keras)',
        dataset_info='Structured loan applicant records containing income, credit, employment, loan, and demographic features. Data is cleaned, encoded, scaled where required, and split for reproducible model evaluation.',
        results='86%+ prediction accuracy, automated EMI and DTI calculations, model comparison benchmarks, and a deployed Django workflow.',
        challenges='Handling class imbalance, preventing data leakage during preprocessing, and balancing model accuracy with understandable risk explanations.',
        future_improvements='Add calibrated probabilities, explainability with SHAP, fairness checks across demographic groups, and monitoring for model drift.',
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
        problem_statement='Candidates need realistic interview practice and actionable feedback that reflects both their resume and the target job description.',
        solution='The platform parses resume and job-description text, generates role-specific questions with an LLM, evaluates answers with NLP similarity and rubric signals, and presents a performance summary.',
        architecture='React frontend; Django/Python application services; NLP preprocessing with spaCy/NLTK; OpenAI API for question generation and evaluation; MySQL for users, sessions, and reports; Spring Boot service integration.',
        features='Resume and job-description analysis; dynamic interview question generation; answer scoring; resume-to-job matching; skill-gap reporting; performance history.',
        features_list=['Extract skills and requirements from resume and job description', 'Generate role-specific technical and behavioral questions', 'Evaluate answers with NLP and rubric-based scoring', 'Identify missing or weak skills', 'Track interview sessions and performance trends'],
        algorithm='NLP (spaCy/NLTK), OpenAI GPT for question generation and answer scoring, cosine similarity',
        dataset_info='User-provided resumes, job descriptions, interview questions, and answers form the application data. Text is processed for each session and stored with the associated evaluation results.',
        results='Real-time interview scoring, resume–JD match scoring, skill gap identification.',
        challenges='Generating relevant questions, keeping evaluation consistent across answer styles, and giving useful feedback without overclaiming human-level assessment.',
        future_improvements='Add speech transcription, interviewer-configurable rubrics, stronger evaluation benchmarks, privacy controls, and multilingual interview support.',
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
        problem_statement='Insurance premiums vary across demographic and health-related factors, making it useful to understand cost drivers before estimating a premium.',
        solution='An exploratory analysis and Linear Regression pipeline cleans the medical-cost data, engineers useful features, visualizes relationships, and serves predictions through a Django interface.',
        architecture='Pandas and NumPy data pipeline; Seaborn and Matplotlib analysis layer; Scikit-learn regression model; Django web interface; SQL-ready application structure.',
        features='Data cleaning; exploratory visual analysis; categorical feature encoding; regression training; prediction form; model-driven insurance cost estimate.',
        features_list=['Explore 1,300+ healthcare records', 'Analyze cost relationships with visualizations', 'Encode categorical demographic and health features', 'Train and evaluate a Linear Regression model', 'Expose predictions through a Django web interface'],
        algorithm='Linear Regression, EDA, Feature Engineering',
        dataset_info='The project uses a healthcare insurance dataset with demographic, family, BMI, smoking, region, and medical-cost fields. More than 1,300 records are analyzed during EDA and model development.',
        results='High accuracy linear model; EDA revealed key price drivers: smoking, BMI, region.',
        challenges='Capturing nonlinear cost effects with a simple baseline model and handling the strong premium impact of smoking status and BMI.',
        future_improvements='Compare regularized and tree-based regressors, add uncertainty intervals, improve validation, and monitor prediction error by subgroup.',
        github_url='https://github.com/Dhanaraj2410/InsurePredict-Insurance-Cost-Prediction-using-Linear-Regression',
        live_demo_url='',
        screenshot=_File(''),
        is_featured=True,
        order=4,
        technologies=_All([SimpleNamespace(name='Python'), SimpleNamespace(name='Pandas'), SimpleNamespace(name='Seaborn'), SimpleNamespace(name='Scikit-learn'), SimpleNamespace(name='Django'), SimpleNamespace(name='SQL')]),
        workflow_steps=_All([]),
    ),
    SimpleNamespace(
        title='Apple Product Pricing Dashboard',
        slug='apple-product-pricing-dashboard',
        short_description='Interactive Power BI dashboard for Apple product pricing, KPI analysis, and business reporting using Power Query, DAX, and star-schema modeling.',
        description='Built an interactive business intelligence dashboard for analyzing Apple product pricing and key performance indicators. Used Power Query for transformation, DAX for reusable measures, and star-schema modeling for clear reporting.',
        problem_statement='Apple product pricing and KPI data can be difficult to compare consistently across product families, storage variants, and reporting periods.',
        solution='A Power BI model standardizes the source data, organizes it into a star schema, and uses DAX measures to provide interactive product and pricing analysis.',
        architecture='Power Query ingestion and transformation; star-schema semantic model; DAX measures and calculated columns; interactive Power BI report pages with slicers and KPI cards.',
        features='Product and model comparison; price and KPI analysis; filterable report views; reusable DAX measures; clear business-facing visual reporting.',
        features_list=['Clean and standardize product and pricing data in Power Query', 'Model product, category, and pricing relationships with a star schema', 'Create reusable DAX measures for KPIs', 'Compare product families and configuration variants', 'Use slicers and interactive visuals for decision support'],
        algorithm='Power Query, DAX, Star Schema',
        dataset_info='Apple product catalog and pricing records organized by product family, model, configuration, and reporting attributes. The model is designed for repeatable refresh when updated source data is available.',
        results='Interactive pricing analysis, reusable KPI measures, structured star-schema reporting, and a clearer comparison workflow for business users.',
        challenges='Keeping product variants consistent, defining measures that remain meaningful across filters, and presenting dense pricing data without clutter.',
        future_improvements='Add scheduled refresh, price-trend tracking, market comparison data, drill-through pages, and a published Power BI service workspace.',
        github_url='https://github.com/Dhanaraj2410',
        live_demo_url='',
        screenshot=_File(''),
        is_featured=True,
        order=5,
        technologies=_All([SimpleNamespace(name='Power BI'), SimpleNamespace(name='Power Query'), SimpleNamespace(name='DAX'), SimpleNamespace(name='Star Schema'), SimpleNamespace(name='Excel')]),
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
    SimpleNamespace(name='Computer Vision', category='ML_AI', category_display='ML_AI', proficiency=60, icon='', order=0),
    SimpleNamespace(name='Tableau (Basics)', category='TOOL', category_display='TOOL', proficiency=60, icon='', order=0),
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
    SimpleNamespace(role_key='general', title='General AI/ML Resume', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Resume.pdf'), order=1),
    SimpleNamespace(role_key='data-analyst', title='Data Analyst / Business Analyst', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Resume(Data_Analyst).pdf'), order=2),
    SimpleNamespace(role_key='data-science', title='Data Scientist / Data Science', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Resume(AI_DS).pdf'), order=3),
    SimpleNamespace(role_key='machine-learning', title='Machine Learning / AI Engineer', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Resume(AI_ML).pdf'), order=4),
    SimpleNamespace(role_key='python-developer', title='Python Developer', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Resume(Python_Developer).pdf'), order=5),
    SimpleNamespace(role_key='sql-developer', title='SQL Developer', summary='', key_skills='', resume_file=_File('/static/media/resumes/roles/Resume(SQL).pdf'), order=6),
]
