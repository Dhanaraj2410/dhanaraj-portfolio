# 🚀 Hosting & Deployment Guide — Dhanaraj AI/ML Portfolio

Your application is fully configured for production hosting with **WhiteNoise** (static asset management), **Gunicorn** (WSGI web server), **Render Blueprint** (`render.yaml`), **Procfile**, and **Vercel Serverless configuration** (`vercel.json`).

---

## 🌟 Option 1: Host Full-Stack Django App on Render.com (Recommended — 100% Free)

**Render** gives you a free live URL (e.g., `https://dhanaraj-portfolio.onrender.com`) with PostgreSQL/SQLite, Gunicorn, and full Django Admin access.

### Step-by-Step Render Deployment:
1. **Push your project to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Deploying Dhanaraj AI/ML Portfolio"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/dhanaraj-portfolio.git
   git push -u origin main
   ```
2. **Go to Render**:
   - Sign up at [Render.com](https://render.com/).
   - Click **New +** → **Web Service**.
   - Connect your GitHub repository `dhanaraj-portfolio`.
3. **Configure Settings**:
   - **Root Directory**: `portfolio`
   - **Runtime**: `Python 3`
   - **Build Command**:
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py seed_data
     ```
   - **Start Command**:
     ```bash
     gunicorn config.wsgi:application
     ```
4. **Environment Variables**:
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `*`
   - `SECRET_KEY`: `(click Generate)`
5. Click **Create Web Service**! Render will build and launch your live site automatically!

---

## ⚡ Option 2: Host Static Single Page App on GitHub Pages / Vercel / Netlify (Instant & Free)

If you want to host the standalone `index.html` static site:

### A. Deploy via GitHub Pages:
1. Go to your GitHub repository settings.
2. Navigate to **Pages** → Source: **Deploy from a branch**.
3. Select `main` branch / `/root` folder and click **Save**.
4. Your site will be live at `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`.

### B. Deploy via Vercel:
1. Sign up at [Vercel.com](https://vercel.com/).
2. Import your GitHub repository.
3. Click **Deploy**! (Vercel automatically detects `index.html` or `portfolio/vercel.json`).

---

## 🔑 Post-Deployment Steps (Admin Setup):
After deploying on Render:
1. Create a Superuser for Django Admin:
   - In Render Dashboard → Click **Shell** → Run:
     ```bash
     python manage.py createsuperuser
     ```
2. Log into Admin at `https://your-site.onrender.com/admin/` to upload custom resumes, certifications, or update your profile picture!
