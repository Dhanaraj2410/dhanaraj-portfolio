# Dhanaraj Portfolio & Career Showcase Platform

A modern, professional, interactive full-stack portfolio platform for **Dhanaraj Arjun Lokhande** — an aspiring AI/ML Engineer and Data Scientist. Built with Django, Django REST Framework, and a premium glassmorphic UI.

## 🚀 Features

| Feature | Description |
|---|---|
| **Single-Page Portfolio** | Hero, About, Resume, Skills, Projects, Experience, Certifications, GitHub, Activities |
| **Django Admin Panel** | Update all content without changing code |
| **REST API** | Full API at `/api/` for all portfolio data |
| **AI Chatbot** | "Ask Dhanaraj AI" — answers questions about the profile |
| **Resume Analyzer** | Paste a job description to get a skill match analysis |
| **GitHub Integration** | Live GitHub data with 1-hour caching |
| **Dark/Light Mode** | Theme toggle with localStorage persistence |
| **Recruiter Dashboard** | Quick candidate snapshot for hiring managers |
| **ML Workflow Visualization** | Animated pipeline for each project |
| **Responsive Design** | Works on desktop, tablet, and mobile (375px–1920px) |
| **SEO Optimized** | Meta tags, Open Graph, JSON-LD, sitemap, robots.txt |

## 📋 Prerequisites

- Python 3.10+
- pip

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd portfolio
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and set:
# - SECRET_KEY (generate a strong key for production)
# - GITHUB_USERNAME (your GitHub username)
# - OPENAI_API_KEY (optional, for AI chatbot/analyzer)
# - GITHUB_TOKEN (optional, for higher API rate limits)
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Seed the Database with Resume Data

```bash
python manage.py seed_data
```

### 7. Create Admin Superuser

```bash
python manage.py createsuperuser
```

### 8. Start Development Server

```bash
python manage.py runserver
```

Visit:
- **Portfolio**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **API Root**: http://127.0.0.1:8000/api/

## 📂 Project Structure

```
portfolio/
├── manage.py
├── config/               # Django settings & URL routing
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/                 # Main portfolio app
│   ├── models.py         # 14 Django models
│   ├── admin.py          # Rich admin interface
│   ├── views.py          # Template views
│   ├── api_views.py      # REST API endpoints
│   ├── serializers.py    # DRF serializers
│   ├── forms.py          # Contact form
│   ├── urls.py           # URL routing
│   ├── sitemaps.py       # SEO sitemaps
│   └── management/commands/seed_data.py
├── ai_assistant/         # AI chatbot & resume analyzer
│   ├── services.py       # OpenAI + fallback logic
│   ├── views.py          # API endpoints
│   └── urls.py
├── github_integration/   # GitHub API proxy
│   ├── services.py       # Fetching + caching
│   ├── views.py          # API endpoint
│   └── urls.py
├── templates/            # Django templates
│   ├── base.html
│   ├── home.html
│   ├── project_detail.html
│   └── robots.txt
├── static/
│   ├── css/style.css     # Design system
│   └── js/
│       ├── main.js       # Core interactions
│       ├── chatbot.js    # AI chatbot widget
│       ├── resume-analyzer.js
│       └── workflow.js   # ML pipeline visualization
├── media/                # Uploaded files
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/` | GET | API overview |
| `/api/profile/` | GET | Profile data |
| `/api/education/` | GET | Education list |
| `/api/experience/` | GET | Experience list |
| `/api/projects/` | GET | All projects |
| `/api/projects/<slug>/` | GET | Project detail |
| `/api/skills/` | GET | Skills list |
| `/api/certifications/` | GET | Certifications |
| `/api/activities/` | GET | Activities |
| `/api/contact/` | POST | Submit contact message |
| `/api/ai/chat/` | POST | AI chatbot |
| `/api/ai/resume-analysis/` | POST | Resume analyzer |
| `/api/github/` | GET | GitHub data |

## 🔧 Django Admin

Log in at `/admin/` to manage:
- **Profile** — Name, bio, photo, resume PDF
- **Education** — Degrees, institutions, scores
- **Experience** — Internships, roles, responsibilities
- **Projects** — Full project details, technologies, workflows
- **Skills** — Categories, proficiency levels
- **Certifications** — Titles, organizations, certificates
- **Activities** — Career activities timeline
- **Social Links** — GitHub, LinkedIn, etc.
- **Contact Messages** — View recruiter messages
- **Site Settings** — Taglines, GitHub username, meta description

## 🤖 AI Features

### Chatbot (Ask Dhanaraj AI)
- Click the 🤖 button in the bottom-right
- Uses OpenAI API if `OPENAI_API_KEY` is set
- Falls back to rule-based responses otherwise

### Resume Analyzer
- Scroll to "AI Resume Analyzer" section
- Paste a job description
- Get skill match %, matching/missing skills, relevant projects

## 🔒 Security

- CSRF protection on all forms
- Environment variables for secrets
- Honeypot spam protection
- Rate limiting on AI endpoints
- Production security headers when `DEBUG=False`
- API keys never exposed to frontend

## 🚀 Production Deployment

1. Set `DEBUG=False` in `.env`
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Set up PostgreSQL and update `DATABASES`
5. Run `python manage.py collectstatic`
6. Use Gunicorn: `gunicorn config.wsgi:application`
7. Set up Nginx as reverse proxy
8. Enable HTTPS

## 📄 License

This project is for personal portfolio use by Dhanaraj Arjun Lokhande.
