"""
Template views for the portfolio website.
"""
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token
from .models import (
    SiteSettings, Profile, Education, Experience, Project,
    Skill, Certification, Activity, Achievement, SocialLink, JobRole, RoleResume,
)
from .forms import ContactForm


def home(request):
    """Render the full single-page portfolio."""
    settings = SiteSettings.load()
    profile = Profile.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    projects = Project.objects.prefetch_related('technologies', 'workflow_steps').all()
    featured_projects = projects.filter(is_featured=True)
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    activities = Activity.objects.all()
    achievements = Achievement.objects.all()
    social_links = SocialLink.objects.all()
    job_roles = JobRole.objects.all()
    role_resumes = RoleResume.objects.all()
    contact_form = ContactForm()

    # Map role_resumes by role_key
    role_resumes_map = {rr.role_key: rr for rr in role_resumes}

    # Group skills by category
    skill_categories = {}
    for skill in skills:
        cat_display = skill.get_category_display()
        if cat_display not in skill_categories:
            skill_categories[cat_display] = []
        skill_categories[cat_display].append(skill)

    # Group activities by category
    activity_categories = {}
    for activity in activities:
        cat_display = activity.get_category_display()
        if cat_display not in activity_categories:
            activity_categories[cat_display] = []
        activity_categories[cat_display].append(activity)

    # Stats for animated counters
    stats = {
        'graduation_year': '2026',
        'cgpa': '8.54',
        'projects_count': projects.count(),
        'internships_count': experience.count(),
        'certifications_count': certifications.count(),
        'primary_skills': 'Python / ML / SQL',
    }

    context = {
        'settings': settings,
        'profile': profile,
        'education': education,
        'experience': experience,
        'projects': projects,
        'featured_projects': featured_projects if featured_projects.exists() else projects[:3],
        'skills': skills,
        'skill_categories': skill_categories,
        'certifications': certifications,
        'activities': activities,
        'activity_categories': activity_categories,
        'achievements': achievements,
        'social_links': social_links,
        'job_roles': job_roles,
        'role_resumes': role_resumes,
        'role_resumes_map': role_resumes_map,
        'contact_form': contact_form,
        'stats': stats,
    }
    return render(request, 'home.html', context)


def project_detail(request, slug):
    """Render a detailed project page."""
    project = get_object_or_404(
        Project.objects.prefetch_related('technologies', 'workflow_steps'),
        slug=slug,
    )
    settings = SiteSettings.load()
    profile = Profile.objects.first()
    social_links = SocialLink.objects.all()

    context = {
        'project': project,
        'settings': settings,
        'profile': profile,
        'social_links': social_links,
    }
    return render(request, 'project_detail.html', context)


import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)


@require_POST
def contact_submit(request):
    """Handle contact form submission via AJAX."""
    form = ContactForm(request.POST)
    if form.is_valid():
        msg_obj = form.save()

        # Send email notification if SMTP is configured
        try:
            admin_email = getattr(settings, 'EMAIL_HOST_USER', '') or 'lokhandedhanraj2410@gmail.com'
            if getattr(settings, 'EMAIL_HOST', None):
                send_mail(
                    subject=f"New Portfolio Contact Message from {msg_obj.name}",
                    message=f"Name: {msg_obj.name}\nEmail: {msg_obj.email}\nCompany: {msg_obj.company}\nRole: {msg_obj.job_role}\n\nMessage:\n{msg_obj.message}",
                    from_email=admin_email,
                    recipient_list=[admin_email],
                    fail_silently=True,
                )
        except Exception as e:
            logger.warning(f"Could not send email notification: {e}")

        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.',
        })
    else:
        errors = {}
        for field, error_list in form.errors.items():
            errors[field] = [str(e) for e in error_list]
        return JsonResponse({
            'success': False,
            'errors': errors,
        }, status=400)


def robots_txt(request):
    """Serve robots.txt."""
    return render(request, 'robots.txt', content_type='text/plain')
