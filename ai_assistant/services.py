"""
AI Assistant services — chatbot and job description analyzer.
Provides recruiter-oriented answers, job description vs. profile analysis,
and deep answers for resume, skills, and projects.
"""
import json
import logging
import re
from django.conf import settings

logger = logging.getLogger(__name__)


def _get_profile_context():
    """Build a comprehensive context string from the database for the AI assistant."""
    from core.models import (
        Profile, Education, Experience, Project, Skill,
        Certification, Activity, SocialLink, JobRole, RoleResume
    )

    parts = []

    profile = Profile.objects.first()
    if profile:
        parts.append("=== CANDIDATE MASTER PROFILE ===")
        parts.append(f"Name: {profile.full_name}")
        parts.append(f"Target Role: {profile.title}")
        parts.append("Status: 2026 Fresh Graduate (B.E. Information Technology)")
        parts.append("University: Savitribai Phule Pune University (SPPU)")
        parts.append("CGPA: 8.54 / 10.0")
        parts.append(f"Location: {profile.location}")
        parts.append(f"Email: {profile.email}")
        parts.append(f"Phone: {profile.phone}")
        parts.append(f"Summary: {profile.bio}")

    education = Education.objects.all()
    if education.exists():
        parts.append("\n=== ACADEMIC EDUCATION ===")
        for edu in education:
            score = f" (Score: {edu.score_display})" if edu.score_display else ""
            parts.append(f"  - {edu.degree} | {edu.institution}{score} [{edu.start_year or ''}-{edu.end_year or ''}]")

    experience = Experience.objects.all()
    if experience.exists():
        parts.append("\n=== WORK EXPERIENCE & INTERNSHIPS ===")
        for exp in experience:
            status = " [Currently Active]" if exp.is_current else ""
            parts.append(f"  - {exp.title} at {exp.company}, {exp.location}{status} ({exp.duration_display})")
            for resp in exp.responsibilities_list:
                parts.append(f"    • {resp}")

    projects = Project.objects.prefetch_related('technologies').all()
    if projects.exists():
        parts.append("\n=== MAJOR FEATURED PROJECTS ===")
        for proj in projects:
            techs = ', '.join(t.name for t in proj.technologies.all())
            parts.append(f"  - {proj.title}")
            parts.append(f"    Tech Stack: {techs}")
            if proj.algorithm:
                parts.append(f"    Algorithm/Model: {proj.algorithm}")
            parts.append(f"    Overview: {proj.short_description}")
            if proj.results:
                parts.append(f"    Key Metrics/Results: {proj.results}")

    skills = Skill.objects.all()
    if skills.exists():
        parts.append("\n=== TECHNICAL COMPETENCIES ===")
        categories = {}
        for skill in skills:
            cat = skill.get_category_display()
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(f"{skill.name} ({skill.proficiency}%)")
        for cat, skill_names in categories.items():
            parts.append(f"  {cat}: {', '.join(skill_names)}")

    certifications = Certification.objects.all()
    if certifications.exists():
        parts.append("\n=== PROFESSIONAL CERTIFICATIONS ===")
        for cert in certifications:
            parts.append(f"  - {cert.title} by {cert.organization}")

    role_resumes = RoleResume.objects.all()
    if role_resumes.exists():
        parts.append("\n=== TARGET JOB ROLES WITH TAILORED RESUMES ===")
        for rr in role_resumes:
            admin_status = "Admin File Uploaded" if rr.resume_file else "Default Generated"
            parts.append(f"  - {rr.get_role_key_display()}: {rr.summary} [{admin_status}]")

    return '\n'.join(parts)


def chat_with_ai(user_message):
    """
    Process a chat message. Checks if message is a Job Description analysis request
    or general resume/recruiter question. Uses OpenAI API if key available, else smart fallback.
    """
    msg_lower = user_message.lower()

    # Check if user is asking for Job Description vs Profile analysis
    if _is_job_description_query(user_message):
        return analyze_resume_match(user_message)

    if getattr(settings, 'OPENAI_API_KEY', None):
        return _openai_chat(user_message)
    return _recruiter_smart_chat(user_message)


def _is_job_description_query(text):
    """Detect if input text contains a job description or JD comparison request."""
    lower = text.lower()
    jd_keywords = ['job description', 'responsibilities:', 'requirements:', 'looking for', 'qualification', 'skills required', 'we are hiring', 'candidate should']
    if any(kw in lower for kw in jd_keywords):
        return True
    # If text is long (> 200 chars) and contains technical terms, treat as JD
    tech_count = sum(1 for word in ['python', 'sql', 'django', 'pandas', 'machine learning', 'data analyst', 'developer', 'react', 'mysql'] if word in lower)
    if len(text) > 250 and tech_count >= 2:
        return True
    return False


def _openai_chat(user_message):
    """Chat using OpenAI API with recruiter-oriented system prompt."""
    try:
        from openai import OpenAI
        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        profile_context = _get_profile_context()
        system_prompt = (
            "You are 'Ask Dhanaraj AI', an executive recruiter assistant representing Dhanaraj Arjun Lokhande. "
            "Dhanaraj is a top 2026 Fresh Graduate (B.E. IT from SPPU with 8.54 CGPA) targeting entry-level roles in: "
            "1. Python Developer, 2. Data Analyst / Business Analyst, 3. Data Science, 4. AI/ML Engineer, 5. SQL Developer.\n"
            "Your responses MUST be professional, recruiter-oriented, concise, and structured. "
            "Always highlight his academic excellence, active internships at Technoworld Softwares & QSpiders, "
            "and IIT Roorkee certification when relevant.\n\n"
            f"CANDIDATE DATA:\n{profile_context}"
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            max_tokens=600,
            temperature=0.6,
        )
        return {
            'success': True,
            'response': response.choices[0].message.content,
        }
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        return _recruiter_smart_chat(user_message)


def _recruiter_smart_chat(user_message):
    """Smart recruiter-oriented fallback chatbot."""
    from core.models import Profile, Project, Skill, Certification, Experience, RoleResume

    msg = user_message.lower()
    profile = Profile.objects.first()
    name = profile.full_name if profile else "Dhanaraj Arjun Lokhande"

    # 1. Job Description vs Profile Analysis request
    if _is_job_description_query(user_message):
        return analyze_resume_match(user_message)

    # 2. Recruiter Overview / Hire Query
    if any(w in msg for w in ['hire', 'why hire', 'recruiter', 'candidate', 'overview', 'fresher', '2026']):
        return {
            'success': True,
            'response': (
                f"🌟 **Recruiter Executive Summary — {name}**\n\n"
                "🎓 **Status:** 2026 Fresh Graduate | B.E. IT at SPPU (8.54 CGPA)\n"
                "💼 **Current Internships:** Data Science Intern @ Technoworld Softwares & Python Developer Intern @ QSpiders\n"
                "📜 **Certification:** IIT Roorkee Certified in Data Science & AI\n"
                "🎯 **Target Entry-Level Roles:** Python Developer | Data Analyst | Data Science | AI/ML Engineer | SQL Developer\n\n"
                "✨ **Key Value Proposition:** Strong mathematical and coding foundation, hands-on production ML project experience, "
                "and immediate availability for full-time opportunities!"
            )
        }

    # 3. Project Questions
    if any(w in msg for w in ['project', 'built', 'developed', 'interview platform', 'insurepredict', 'loan']):
        projects = Project.objects.all()
        lines = []
        for p in projects:
            lines.append(f"• **{p.title}**\n  - Tech: {p.short_description}\n  - Algorithm: {p.algorithm if p.algorithm else 'NLP & ML Architecture'}")
        return {
            'success': True,
            'response': (
                f"🔨 **Dhanaraj's Major Projects ({projects.count()} Production Builds):**\n\n" +
                '\n\n'.join(lines) +
                "\n\n💡 *All project code and live ML simulators are accessible directly on this portfolio!*"
            )
        }

    # 4. Skill Questions
    if any(w in msg for w in ['skill', 'technology', 'stack', 'python', 'sql', 'power bi', 'django', 'scikit']):
        return {
            'success': True,
            'response': (
                f"⚡ **Technical Skills Breakdown for {name}:**\n\n"
                "🐍 **Languages:** Python (Advanced), SQL (MySQL), JavaScript, HTML5/CSS3\n"
                "🤖 **ML & AI:** Scikit-learn, TensorFlow, Keras, NLP, OpenAI API, Feature Engineering\n"
                "📊 **Data & BI:** Pandas, NumPy, Matplotlib, Seaborn, Power BI, Excel Charts\n"
                "🏗️ **Backend & Web:** Django, RESTful APIs, MySQL Workbench, Git & GitHub\n\n"
                "🎓 Certified by **IIT Roorkee (Data Science & AI)** and **Intellipaat (SQL)**."
            )
        }

    # 5. Internships & Experience
    if any(w in msg for w in ['experience', 'intern', 'company', 'technoworld', 'qspiders', 'work']):
        exps = Experience.objects.all()
        exp_text = []
        for e in exps:
            exp_text.append(f"• **{e.title}** at *{e.company}* ({e.duration_display})\n  Location: {e.location}\n  Focus: {e.description}")
        return {
            'success': True,
            'response': "💼 **Practical Industry Experience:**\n\n" + '\n\n'.join(exp_text)
        }

    # 6. Certifications
    if any(w in msg for w in ['certification', 'certified', 'iit', 'intellipaat', 'power bi']):
        certs = Certification.objects.all()
        c_lines = [f"• **{c.title}** — *{c.organization}*" for c in certs]
        return {
            'success': True,
            'response': "📜 **Verified Professional Credentials:**\n\n" + '\n'.join(c_lines)
        }

    # 7. Education & Academics
    if any(w in msg for w in ['education', 'degree', 'cgpa', 'sppu', 'college', 'university', 'academic']):
        return {
            'success': True,
            'response': (
                f"🎓 **Academic Background:**\n\n"
                "• **Degree:** Bachelor of Engineering in Information Technology\n"
                "• **University:** Savitribai Phule Pune University (SPPU)\n"
                "• **Academic CGPA:** **8.54 / 10.0** (Top Academic Performer)\n"
                "• **Graduating Batch:** **2026 Batch**"
            )
        }

    # 8. Contact & Availability
    if any(w in msg for w in ['contact', 'email', 'phone', 'location', 'reach', 'address']):
        return {
            'success': True,
            'response': (
                f"📬 **Contact Details for Hiring & Inquiries:**\n\n"
                f"📧 **Email:** lokhandedhanraj2410@gmail.com\n"
                f"📱 **Phone:** +91 7507855698\n"
                f"📍 **Location:** Pune, Maharashtra, India\n"
                f"💼 **LinkedIn:** linkedin.com/in/dhanaraj-lokhande-a27536283\n"
                f"🐙 **GitHub:** github.com/DhanarajLokhande"
            )
        }

    # Default Recruiter Response
    return {
        'success': True,
        'response': (
            f"👋 Hi! I'm **Ask Dhanaraj AI**.\n\n"
            f"I can assist recruiters and visitors with:\n"
            "• **Job Description Analysis**: Paste any JD to evaluate candidate alignment!\n"
            "• **Skills & Tech Stack**: Questions on Python, SQL, ML, Power BI, Django.\n"
            "• **Projects & Demos**: Details on AI Mock Interview, InsurePredict, Loan System.\n"
            "• **Academic & Work Profile**: 8.54 CGPA, SPPU, Technoworld Softwares & QSpiders internships.\n\n"
            "What would you like to know?"
        )
    }


def analyze_resume_match(job_description):
    """
    Perform a Job Description vs. Candidate Profile Analysis.
    Calculates match score, matched core skills, missing keywords, and recruiter recommendation.
    """
    if getattr(settings, 'OPENAI_API_KEY', None):
        try:
            from openai import OpenAI
            client = OpenAI(api_key=settings.OPENAI_API_KEY)

            profile_context = _get_profile_context()
            system_prompt = (
                "You are an expert technical recruiter analyzing job alignment for candidate Dhanaraj Arjun Lokhande. "
                "Evaluate the provided Job Description against Dhanaraj's 2026 Fresher profile (B.E. IT 8.54 CGPA, "
                "Data Science & Python Internships, IIT Certified, Python, SQL, ML, Django, Power BI skills).\n"
                "Provide a structured analysis containing:\n"
                "1. Overall Alignment Match Score (0-100%)\n"
                "2. Matched Key Skills & Strengths\n"
                "3. Missing Keywords / Gaps\n"
                "4. Final Hiring Recommendation for 2026 Fresher Position."
            )

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"JOB DESCRIPTION:\n{job_description}"},
                ],
                max_tokens=700,
                temperature=0.5,
            )
            return {
                'success': True,
                'response': response.choices[0].message.content,
            }
        except Exception as e:
            logger.error(f"OpenAI error in resume analysis: {e}")

    # Smart Rule-Based JD Analysis
    lower_jd = job_description.lower()
    
    target_skills = [
        'python', 'sql', 'mysql', 'pandas', 'numpy', 'scikit-learn', 'machine learning',
        'data science', 'data analyst', 'power bi', 'django', 'rest api', 'eda', 'visualization',
        'tableau', 'excel', 'nlp', 'deep learning', 'tensorflow', 'git'
    ]

    matched = [s.upper() for s in target_skills if s in lower_jd]
    missing = [s.title() for s in target_skills if s not in lower_jd][:4]

    score = min(96, max(45, 50 + len(matched) * 4))
    if len(matched) == 0:
        score = 65 # Baseline fresher score

    matched_str = ', '.join(matched) if matched else "PYTHON, SQL, DATA ANALYSIS, 2026 FRESHER"
    missing_str = ', '.join(missing) if missing else "Advanced Cloud Ops"

    report = (
        f"📊 **Job Description vs. Candidate Profile Analysis Report**\n\n"
        f"🎯 **Target Match Score:** **{score}% Alignment**\n\n"
        f"✅ **Matched Key Skills & Strengths:**\n{matched_str}\n\n"
        f"💡 **Complementary Strengths to Highlight:**\n"
        "• B.E. IT 2026 Graduate with 8.54 CGPA from SPPU\n"
        "• Hands-on Data Science Internship at Technoworld Softwares & Python Intern at QSpiders\n"
        "• IIT Roorkee Certification in Data Science & AI\n\n"
        f"📌 **Suggested Keywords to Emphasize:**\n{missing_str}\n\n"
        f"🏆 **Recruiter Verdict:**\n"
        f"Dhanaraj is a **highly qualified 2026 entry-level candidate** for this position, demonstrating strong core technical capabilities and quick adaptability."
    )

    return {
        'success': True,
        'response': report,
    }
