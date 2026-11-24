"""
Template views for the portfolio website (static, no database).
All content is served from core/content.py.
"""
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from . import content


def _group(items, attr):
    groups = {}
    for item in items:
        key = getattr(item, attr)
        groups.setdefault(key, []).append(item)
    return groups


def home(request):
    """Render the full single-page portfolio."""
    projects = content.PROJECTS
    featured = [p for p in projects if p.is_featured]

    stats = {
        'graduation_year': '2026',
        'cgpa': '8.54',
        'projects_count': len(projects),
        'internships_count': len(content.EXPERIENCE),
        'certifications_count': len(content.CERTIFICATIONS),
        'primary_skills': 'Python / ML / GenAI / SQL',
    }

    context = {
        'settings': content.SITE,
        'profile': content.PROFILE,
        'education': content.EDUCATION,
        'experience': content.EXPERIENCE,
        'projects': projects,
        'featured_projects': featured if featured else projects[:3],
        'skills': content.SKILLS,
        'skill_categories': _group(content.SKILLS, 'category_display'),
        'certifications': content.CERTIFICATIONS,
        'activities': content.ACTIVITIES,
        'activity_categories': _group(content.ACTIVITIES, 'category_display'),
        'achievements': content.ACHIEVEMENTS,
        'social_links': content.SOCIAL_LINKS,
        'job_roles': content.JOB_ROLES,
        'role_resumes': content.ROLE_RESUMES,
        'role_resumes_map': {rr.role_key: rr for rr in content.ROLE_RESUMES},
        'stats': stats,
    }
    return render(request, 'home.html', context)


def project_detail(request, slug):
    """Render a detailed project page."""
    project = next((p for p in content.PROJECTS if p.slug == slug), None)
    if project is None:
        raise Http404('Project not found')

    context = {
        'project': project,
        'settings': content.SITE,
        'profile': content.PROFILE,
        'social_links': content.SOCIAL_LINKS,
    }
    return render(request, 'project_detail.html', context)


@require_POST
def contact_submit(request):
    """Contact submissions are not stored (no database).

    The contact section links directly to the owner's email and social profiles.
    """
    return JsonResponse({
        'success': True,
        'message': 'Thanks! Please email lokhandedhanraj2410@gmail.com directly.',
    })


def robots_txt(request):
    """Serve robots.txt."""
    return render(request, 'robots.txt', content_type='text/plain')