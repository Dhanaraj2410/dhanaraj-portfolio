# 🚀 Hosting & Deployment Guide — Dhanaraj AI/ML Portfolio

Your application is configured and pushed to GitHub:
👉 **Repository**: `https://github.com/Dhanaraj2410/dhanaraj-portfolio`

---

## 🌟 Deploy on Render.com (100% Free Full-Stack Web Service)

Render will host your full-stack Django site live at `https://dhanaraj-portfolio.onrender.com`.

### Step-by-Step Render Deployment:
1. Go to **[Render Dashboard](https://dashboard.render.com/)**.
2. Click **New +** → **Web Service**.
3. Connect your repository: **`Dhanaraj2410/dhanaraj-portfolio`**.
4. Configure these fields:
   - **Name**: `dhanaraj-portfolio`
   - **Branch**: `main`
   - **Root Directory**: *(leave blank)*
   - **Runtime**: `Python 3`
   - **Build Command**:
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py seed_data
     ```
   - **Start Command**:
     ```bash
     gunicorn config.wsgi:application
     ```
   - **Instance Type**: `Free`
5. **Environment Variables**:
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `*`
   - `SECRET_KEY`: `(click Generate)`
6. Click **Create Web Service**! Render will deploy your application automatically.

---

## 🔑 Admin Setup After Deployment:
In Render Dashboard → Click your web service → **Shell** → Run:
```bash
python manage.py createsuperuser
```
Then log in at `https://dhanaraj-portfolio.onrender.com/admin/` to upload custom resumes, certifications, or update your profile photo!
