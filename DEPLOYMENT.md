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
   - `ALLOWED_HOSTS`: `dhanaraj-portfolio.onrender.com` (include any custom domain)
   - `SECRET_KEY`: `(click Generate)`
   - Configure `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`,
     and `EMAIL_USE_TLS` to enable contact notifications. Set `CONTACT_EMAIL` if
     notifications should go to a different address.
6. Click **Create Web Service**! Render will deploy your application automatically.

The app uses MySQL by default. For persistent production data, configure a managed
database and set `DB_ENGINE=mysql`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`,
and `DB_PORT` in the service's environment settings. Enable `DB_SSL=True` when
required by the provider; set `DB_SSL_CA` to its CA certificate path when supplied.
Alternatively, set `DATABASE_URL` to a provider-supported database URL. Never commit
database credentials.

## 🌐 Deploy on Vercel

Vercel's function filesystem is not a persistent database. Use a remotely hosted
MySQL service; do not set its host to `localhost`. In Vercel Project Settings →
Environment Variables, add the production `DB_ENGINE=mysql`, `DB_NAME`, `DB_USER`,
`DB_PASSWORD`, `DB_HOST`, and `DB_PORT`. Set `DB_SSL=True` and, if required by the
provider, provide `DB_SSL_CA` using the provider's recommended certificate setup.
Keep these values in Vercel's environment settings, not in the repository or
`vercel.json`. A MySQL `DATABASE_URL` can be used instead when supported by the
provider.

Set the Vercel project's Root Directory to `portfolio` so it uses
`portfolio/vercel.json` and `portfolio/requirements.txt`. Run `python manage.py
migrate` against the remote database from a trusted environment after its
environment variables are configured and before serving the new version. Do not
run schema migrations from every serverless function invocation. Create an admin
user through a trusted environment with the same production database settings:

```bash
python manage.py createsuperuser
```

For ongoing schema changes, generate and review migrations locally, then apply
them to the production database before deploying code that depends on them.

The Django settings allow `dhanaraj-portfolio-mocha.vercel.app` and trust its HTTPS
origin for CSRF checks. If you configure `ALLOWED_HOSTS` or
`CSRF_TRUSTED_ORIGINS` in Vercel's project environment variables, include the
Vercel hostname and origin respectively:

- `ALLOWED_HOSTS`: `dhanaraj-portfolio-mocha.vercel.app`
- `CSRF_TRUSTED_ORIGINS`: `https://dhanaraj-portfolio-mocha.vercel.app`

For additional custom domains, add each domain to both settings as appropriate.

---

## 🔑 Admin Setup After Deployment:
In Render Dashboard → Click your web service → **Shell** → Run:
```bash
python manage.py createsuperuser
```
Then log in at `https://dhanaraj-portfolio.onrender.com/admin/` to upload custom resumes, certifications, or update your profile photo!
