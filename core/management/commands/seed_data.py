"""
Management command to seed the database with Dhanaraj's actual resume data.
All data sourced directly from the provided resume — nothing fabricated.
"""
from datetime import date
from django.core.management.base import BaseCommand
from core.models import (
    SiteSettings, Profile, Education, Experience, Project,
    ProjectTechnology, ProjectWorkflowStep, Skill, Certification,
    Activity, SocialLink, JobRole, RoleResume,
)


class Command(BaseCommand):
    help = 'Seed the database with portfolio data from resume'

    def handle(self, *args, **options):
        self.stdout.write('Seeding portfolio data...\n')

        # ─── Site Settings ────────────────────────────────────────────
        settings, _ = SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                'site_title': 'Dhanaraj AI/ML Portfolio',
                'tagline': 'AI/ML Engineer | Data Scientist | Python Developer | Data Analyst',
                'secondary_tagline': 'My Skills, Projects, Experience, Certifications & Career Journey — All in One Place.',
                'github_username': 'Dhanaraj2410',
                'linkedin_url': 'https://www.linkedin.com/in/dhanaraj-lokhande2410',
                'meta_description': 'Dhanaraj Arjun Lokhande — AI/ML Engineer & Data Scientist. Portfolio showcasing Python, Machine Learning, Data Science projects, certifications, and career journey.',
            },
        )
        self.stdout.write(self.style.SUCCESS('  [OK] Site Settings'))

        # ─── Profile ─────────────────────────────────────────────────
        profile, _ = Profile.objects.update_or_create(
            pk=1,
            defaults={
                'full_name': 'Dhanaraj Arjun Lokhande',
                'title': 'AI/ML Engineer | Data Scientist',
                'bio': (
                    'AI/ML Engineer and Data Science graduate with strong skills in Python, '
                    'Machine Learning, SQL, and Data Analysis. Passionate about building '
                    'intelligent applications using data-driven approaches. Experienced in '
                    'data preprocessing, EDA, feature engineering, model development, and '
                    'deployment. Skilled in Python, Scikit-learn, Pandas, NumPy, Django, '
                    'and data visualization tools. Currently pursuing a Bachelor of Engineering '
                    'in Information Technology from Savitribai Phule Pune University with a '
                    'CGPA of 8.54. Focused on AI application development, NLP, Deep Learning, '
                    'Generative AI, and real-world problem solving.'
                ),
                'location': 'Pune, Maharashtra, India',
                'email': 'lokhandedhanraj2410@gmail.com',
                'phone': '+91 7507855698',
                'professional_summary': (
                    'AI/ML Engineer and Data Science graduate with strong skills in Python, '
                    'Machine Learning, SQL, and Data Analysis. Experienced in data preprocessing, '
                    'EDA, feature engineering, model development, and deployment using Scikit-learn, '
                    'Pandas, NumPy, and Django.'
                ),
            },
        )
        self.stdout.write(self.style.SUCCESS('  [OK] Profile'))

        # ─── Education ────────────────────────────────────────────────
        Education.objects.all().delete()
        education_data = [
            {
                'degree': 'Bachelor of Engineering – Information Technology',
                'level': 'BE',
                'institution': 'Savitribai Phule Pune University',
                'university': 'Savitribai Phule Pune University',
                'start_year': 2022,
                'end_year': 2026,
                'cgpa': 8.54,
                'order': 1,
            },
            {
                'degree': 'Higher Secondary Certificate (HSC)',
                'level': 'HSC',
                'institution': 'Dhanaji Nana Mahavidyalaya',
                'start_year': 2021,
                'end_year': 2022,
                'percentage': 75.00,
                'order': 2,
            },
            {
                'degree': 'Secondary School Certificate (SSC)',
                'level': 'SSC',
                'institution': 'G.G. Bendale High School',
                'start_year': 2019,
                'end_year': 2020,
                'percentage': 79.20,
                'order': 3,
            },
        ]
        for edu in education_data:
            Education.objects.create(**edu)
        self.stdout.write(self.style.SUCCESS('  [OK] Education (3 entries)'))

        # ─── Experience ───────────────────────────────────────────────
        Experience.objects.all().delete()
        experience_data = [
            {
                'title': 'Data Science Intern',
                'company': 'Technoworld Softwares',
                'location': 'Pune',
                'start_date': date(2026, 2, 1),
                'is_current': True,
                'responsibilities': (
                    'Python programming and scripting\n'
                    'Machine Learning model development and evaluation\n'
                    'Exploratory Data Analysis (EDA)\n'
                    'SQL database queries and operations\n'
                    'Scikit-learn for model building\n'
                    'Working with real-world datasets\n'
                    'Data preprocessing and feature engineering'
                ),
                'order': 1,
            },
            {
                'title': 'Python Developer Intern',
                'company': 'QSpiders',
                'location': 'Pune',
                'start_date': date(2026, 1, 1),
                'is_current': True,
                'responsibilities': (
                    'Python development\n'
                    'Object-Oriented Programming (OOP)\n'
                    'SQL database operations\n'
                    'Mini projects development\n'
                    'Debugging and problem solving'
                ),
                'order': 2,
            },
        ]
        for exp in experience_data:
            Experience.objects.create(**exp)
        self.stdout.write(self.style.SUCCESS('  [OK] Experience (2 internships)'))

        # ─── Projects ────────────────────────────────────────────────
        Project.objects.all().delete()

        # Project 1: AI-Powered Mock Interview Platform
        p1 = Project.objects.create(
            title='AI-Powered Mock Interview Platform',
            slug='ai-mock-interview-platform',
            short_description='AI-based interview platform using Python, Django, NLP, and OpenAI API for automated mock interviews with resume analysis and performance evaluation.',
            description=(
                'Developed an AI-based interview platform using Python, Django, NLP, and OpenAI API. '
                'The platform provides automated mock interviews with intelligent question generation, '
                'answer evaluation, and performance analysis.'
            ),
            problem_statement='Candidates lack access to realistic, AI-powered interview practice that provides structured feedback and evaluation.',
            solution='Built a comprehensive mock interview platform that uses NLP and AI to generate relevant interview questions, evaluate candidate answers, and provide detailed performance feedback.',
            features=(
                'AI mock interviews\n'
                'Resume analysis\n'
                'Automated interview feedback\n'
                'AI-generated questions\n'
                'Answer evaluation\n'
                'Candidate profile\n'
                'Interview history\n'
                'Performance analysis'
            ),
            algorithm='NLP, OpenAI API',
            results='Fully functional interview simulation with AI-driven evaluation',
            challenges='Integrating NLP for accurate answer evaluation and handling diverse interview domains',
            future_improvements='Add multilingual support, video interview capability, and industry-specific question banks',
            is_featured=True,
            order=1,
        )
        for i, tech in enumerate(['Python', 'NLP', 'Machine Learning', 'Django', 'React', 'Spring Boot', 'MySQL', 'OpenAI API']):
            ProjectTechnology.objects.create(project=p1, name=tech, order=i)
        for i, (title, desc) in enumerate([
            ('Candidate', 'User initiates the interview process'),
            ('Resume Upload', 'Candidate uploads their resume'),
            ('Resume Analysis', 'AI analyzes resume content and skills'),
            ('Interview Question Generation', 'AI generates relevant questions based on profile'),
            ('Candidate Answer', 'Candidate provides answers to questions'),
            ('NLP/AI Analysis', 'Natural Language Processing evaluates answers'),
            ('Performance Evaluation', 'System scores and evaluates overall performance'),
            ('Feedback & Score', 'Detailed feedback and score provided to candidate'),
        ]):
            ProjectWorkflowStep.objects.create(project=p1, title=title, description=desc, order=i)

        # Project 2: InsurePredict
        p2 = Project.objects.create(
            title='InsurePredict – Insurance Cost Prediction',
            slug='insurepredict-insurance-cost-prediction',
            short_description='Machine learning system for predicting insurance costs using Linear Regression with 1300+ insurance records, featuring EDA, data preprocessing, and a Django web interface.',
            description=(
                'Built an insurance cost prediction system using Python, Scikit-learn, and Django. '
                'The system uses Linear Regression on 1300+ insurance records to predict costs with '
                'real-time prediction through a web interface.'
            ),
            problem_statement='Insurance companies need accurate cost predictions based on customer attributes for risk assessment and pricing.',
            solution='Developed a machine learning pipeline with comprehensive EDA, data preprocessing, feature engineering, and Linear Regression model deployed through a Django web application.',
            features=(
                '1300+ insurance records dataset\n'
                'Exploratory Data Analysis (EDA)\n'
                'Data preprocessing and cleaning\n'
                'Feature engineering\n'
                'Linear Regression model\n'
                'Real-time prediction interface\n'
                'Django web application'
            ),
            algorithm='Linear Regression',
            dataset_info='1300+ insurance records with features including age, BMI, smoking status, region, and charges',
            results='Accurate insurance cost predictions using Linear Regression model',
            challenges='Handling outliers in insurance data and feature selection for optimal model performance',
            future_improvements='Implement ensemble methods, add more features, deploy as a REST API',
            is_featured=True,
            order=2,
        )
        for i, tech in enumerate(['Python', 'Scikit-learn', 'Django', 'SQL', 'HTML', 'CSS']):
            ProjectTechnology.objects.create(project=p2, name=tech, order=i)
        for i, (title, desc) in enumerate([
            ('Dataset', 'Load 1300+ insurance records'),
            ('Data Cleaning', 'Handle missing values and outliers'),
            ('EDA', 'Exploratory Data Analysis and visualization'),
            ('Feature Engineering', 'Transform and select relevant features'),
            ('Train/Test Split', 'Split data for model training and evaluation'),
            ('Linear Regression', 'Train the prediction model'),
            ('Model Evaluation', 'Evaluate accuracy and metrics'),
            ('Prediction', 'Generate real-time predictions'),
            ('Django Web Application', 'Deploy with interactive web interface'),
        ]):
            ProjectWorkflowStep.objects.create(project=p2, title=title, description=desc, order=i)

        # Project 3: Loan Approval Prediction
        p3 = Project.objects.create(
            title='AI-Powered Loan Approval Prediction System',
            slug='ai-loan-approval-prediction',
            short_description='Machine learning system for predicting loan approval using Logistic Regression with 86% accuracy, featuring user input form and Django backend with MySQL.',
            description=(
                'Built a loan approval prediction system using Python, Django, and Scikit-learn. '
                'The system uses Logistic Regression to predict loan approval with 86% reported accuracy, '
                'featuring a user-friendly input form and real-time predictions.'
            ),
            problem_statement='Banks and financial institutions need automated, data-driven loan approval decisions to reduce processing time and improve accuracy.',
            solution='Developed a machine learning system using Logistic Regression that predicts loan approval based on applicant data, deployed through a Django web application with MySQL database.',
            features=(
                'User input form\n'
                'Data preprocessing\n'
                'ML prediction\n'
                'Real-time prediction\n'
                'Django backend\n'
                'MySQL database\n'
                'Approval/Rejection result display'
            ),
            algorithm='Logistic Regression',
            results='86% reported accuracy on loan approval prediction',
            challenges='Handling imbalanced classes in loan approval data and ensuring model fairness',
            future_improvements='Implement more advanced algorithms, add explainability features, integrate with banking APIs',
            is_featured=True,
            order=3,
        )
        for i, tech in enumerate(['Python', 'Django', 'Machine Learning', 'Scikit-learn', 'MySQL', 'HTML5', 'CSS3', 'JavaScript']):
            ProjectTechnology.objects.create(project=p3, name=tech, order=i)
        for i, (title, desc) in enumerate([
            ('User Input', 'Applicant enters loan details'),
            ('Data Validation', 'Validate and sanitize input data'),
            ('Preprocessing', 'Clean and prepare data for model'),
            ('Feature Transformation', 'Transform features for model input'),
            ('Logistic Regression Model', 'Run prediction model'),
            ('Prediction', 'Generate approval probability'),
            ('Approval / Rejection Result', 'Display decision to user'),
        ]):
            ProjectWorkflowStep.objects.create(project=p3, title=title, description=desc, order=i)

        self.stdout.write(self.style.SUCCESS('  [OK] Projects (3 projects with technologies & workflows)'))

        # ─── Skills ───────────────────────────────────────────────────
        Skill.objects.all().delete()
        skills_data = [
            # Programming
            ('Python', 'PROGRAMMING', 90, 1),
            ('SQL', 'PROGRAMMING', 80, 2),
            ('HTML', 'PROGRAMMING', 80, 3),
            ('CSS', 'PROGRAMMING', 75, 4),
            ('JavaScript', 'PROGRAMMING', 70, 5),
            # Python Libraries
            ('NumPy', 'LIBRARIES', 85, 1),
            ('Pandas', 'LIBRARIES', 85, 2),
            ('Matplotlib', 'LIBRARIES', 80, 3),
            ('Seaborn', 'LIBRARIES', 75, 4),
            ('Scikit-learn', 'LIBRARIES', 85, 5),
            ('TensorFlow', 'LIBRARIES', 65, 6),
            ('Keras', 'LIBRARIES', 65, 7),
            # Machine Learning
            ('Regression', 'ML', 85, 1),
            ('Classification', 'ML', 80, 2),
            ('Feature Engineering', 'ML', 80, 3),
            ('Cross Validation', 'ML', 75, 4),
            ('Hyperparameter Tuning', 'ML', 70, 5),
            ('Model Evaluation', 'ML', 80, 6),
            ('EDA', 'ML', 85, 7),
            # Visualization
            ('Power BI', 'VISUALIZATION', 70, 1),
            ('Matplotlib', 'VISUALIZATION', 80, 2),
            ('Seaborn', 'VISUALIZATION', 75, 3),
            ('Tableau', 'VISUALIZATION', 60, 4),
            ('Excel Charts', 'VISUALIZATION', 70, 5),
            # Developer Tools
            ('Git', 'TOOLS', 75, 1),
            ('GitHub', 'TOOLS', 80, 2),
            ('VS Code', 'TOOLS', 85, 3),
            ('Jupyter Notebook', 'TOOLS', 85, 4),
            ('Google Colab', 'TOOLS', 80, 5),
            # Soft Skills
            ('Business Communication', 'SOFT', 80, 1),
            ('Analytical Thinking', 'SOFT', 85, 2),
            ('Problem Solving', 'SOFT', 85, 3),
            ('Presentation', 'SOFT', 75, 4),
            ('Decision Making', 'SOFT', 80, 5),
            ('Leadership', 'SOFT', 75, 6),
        ]
        for name, category, proficiency, order in skills_data:
            Skill.objects.create(name=name, category=category, proficiency=proficiency, order=order)
        self.stdout.write(self.style.SUCCESS(f'  [OK] Skills ({len(skills_data)} skills)'))

        # ─── Certifications ───────────────────────────────────────────
        Certification.objects.all().delete()
        cert_data = [
            {
                'title': 'Professional Certification in Data Science & Artificial Intelligence',
                'organization': 'Indian Institute of Technology (IIT) Roorkee – iHUB DivyaSampark',
                'skills': 'Data Science\nMachine Learning\nArtificial Intelligence\nHands-on projects',
                'order': 1,
            },
            {
                'title': 'SQL Course Certification',
                'organization': 'Intellipaat',
                'skills': 'SQL queries\nJoins\nFiltering\nSQL operations',
                'order': 2,
            },
            {
                'title': 'Power BI Certification',
                'organization': 'R3 Sys',
                'skills': 'Dashboard design\nBusiness Intelligence',
                'order': 3,
            },
            {
                'title': 'AI Tools and ChatGPT Workshop',
                'organization': 'be10x',
                'skills': 'AI tools\nData analysis\nDebugging\nAutomation',
                'order': 4,
            },
        ]
        for cert in cert_data:
            Certification.objects.create(**cert)
        self.stdout.write(self.style.SUCCESS('  [OK] Certifications (4 certifications)'))

        # ─── Social Links ─────────────────────────────────────────────
        SocialLink.objects.all().delete()
        SocialLink.objects.create(platform='email', url='lokhandedhanraj2410@gmail.com', display_name='Email', order=1)
        SocialLink.objects.create(platform='github', url='https://github.com/Dhanaraj2410', display_name='GitHub', order=2)
        SocialLink.objects.create(platform='linkedin', url='https://www.linkedin.com/in/dhanaraj-lokhande2410', display_name='LinkedIn', order=3)
        self.stdout.write(self.style.SUCCESS('  [OK] Social Links'))

        # ─── Job Roles & Role Resumes ─────────────────────────────────
        JobRole.objects.all().delete()
        roles = [
            'Python Developer',
            'Data Analyst',
            'Data Scientist',
            'Machine Learning Engineer',
            'AI/ML Engineer',
            'Junior AI Engineer',
            'Junior Data Scientist',
            'Python/Django Developer',
        ]
        for i, role in enumerate(roles):
            JobRole.objects.create(title=role, order=i)
        self.stdout.write(self.style.SUCCESS('  [OK] Job Roles (8 Target Roles)'))

        RoleResume.objects.all().delete()
        role_resumes_data = [
            {
                'role_key': 'data-analyst',
                'title': 'Data Analyst / Business Analyst Resume',
                'summary': 'Detail-oriented 2026 IT Fresh Graduate (8.54 CGPA) with hands-on expertise in SQL, Power BI, Excel, Pandas, and Business Analytics.',
                'key_skills': 'SQL, MySQL, Power BI, Python, Pandas, Excel, Tableau, EDA, Business Analytics',
                'order': 1,
            },
            {
                'role_key': 'data-science',
                'title': 'Data Science / Data Scientist Resume',
                'summary': 'Analytical 2026 Fresher (IIT Roorkee Certified in Data Science & AI) with strong capabilities in statistical modeling, machine learning, and feature engineering.',
                'key_skills': 'Python, Scikit-learn, Pandas, NumPy, Regression, Classification, Feature Engineering, EDA',
                'order': 2,
            },
            {
                'role_key': 'machine-learning',
                'title': 'Machine Learning / AI Engineer Resume',
                'summary': 'Innovative 2026 AI/ML Engineer with hands-on experience building, evaluating, and deploying intelligent machine learning and NLP systems.',
                'key_skills': 'Python, Machine Learning, NLP, OpenAI API, GenAI, Scikit-learn, TensorFlow, Django',
                'order': 3,
            },
            {
                'role_key': 'python-developer',
                'title': 'Python Developer / Backend Engineer Resume',
                'summary': 'Core Python 2026 Fresh Graduate (Python Developer Intern at QSpiders) with expertise in OOP, Django, MySQL, and REST APIs.',
                'key_skills': 'Python 3, OOP, Django, REST APIs, MySQL, Data Structures, Git, Modular Code',
                'order': 4,
            },
            {
                'role_key': 'sql-developer',
                'title': 'SQL Developer / Database Analyst Resume',
                'summary': 'Certified SQL Developer (Intellipaat Certified) and 2026 IT Fresher skilled in complex JOINs, subqueries, database schema design, and indexing.',
                'key_skills': 'SQL, MySQL, JOINs, Subqueries, Schema Design, Indexing, Data Modeling, Workbench',
                'order': 5,
            },
        ]
        for r_data in role_resumes_data:
            RoleResume.objects.create(**r_data)
        self.stdout.write(self.style.SUCCESS('  [OK] Role Resumes (5 Roles)'))


        # ─── Activities ───────────────────────────────────────────────
        Activity.objects.all().delete()
        activities_data = [
            ('GitHub Projects & Commits', 'CODING', 'Active GitHub development with ML and Python projects', '💻'),
            ('Python Development', 'CODING', 'Building applications with Python and Django', '🐍'),
            ('ML Experiments', 'CODING', 'Experimenting with ML algorithms and model evaluation', '🧪'),
            ('Machine Learning', 'LEARNING', 'Studying ML algorithms, model evaluation, and deployment', '🤖'),
            ('Deep Learning', 'LEARNING', 'Learning neural networks with TensorFlow and Keras', '🧠'),
            ('NLP', 'LEARNING', 'Natural Language Processing techniques and applications', '📝'),
            ('Generative AI', 'LEARNING', 'Exploring generative AI and large language models', '✨'),
            ('Data Science Internship', 'CAREER', 'Data Science Intern at Technoworld Softwares, Pune', '🏢'),
            ('Python Internship', 'CAREER', 'Python Developer Intern at QSpiders, Pune', '🏢'),
            ('Certifications', 'CAREER', 'Completed 4 professional certifications including IIT Roorkee', '📜'),
            ('AI/ML Projects', 'CAREER', 'Built 3 major AI/ML projects with real-world applications', '🚀'),
        ]
        for i, (title, category, description, icon) in enumerate(activities_data):
            Activity.objects.create(
                title=title, category=category, description=description,
                icon=icon, date=date(2026, 1, 1), order=i,
            )
        self.stdout.write(self.style.SUCCESS('  [OK] Activities'))

        self.stdout.write(self.style.SUCCESS('\n[SUCCESS] Database seeded successfully!'))
        self.stdout.write('  Run the dev server: python manage.py runserver')
        self.stdout.write('  Admin panel: http://127.0.0.1:8000/admin/')
