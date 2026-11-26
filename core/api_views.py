"""
REST API views for the portfolio platform (static, no database).
Content is served from core/content.py.
"""
import requests

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import content


@api_view(['GET'])
def github_api(request):
    """Return GitHub profile data, with a safe local fallback."""
    username = 'Dhanaraj2410'
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'dhanaraj-portfolio'}
    try:
        profile_response = requests.get(
            f'https://api.github.com/users/{username}', headers=headers, timeout=5
        )
        repos_response = requests.get(
            f'https://api.github.com/users/{username}/repos?per_page=100&sort=updated',
            headers=headers,
            timeout=5,
        )
        profile_response.raise_for_status()
        repos_response.raise_for_status()
        profile_data = profile_response.json()
        repositories = [
            {
                'name': repo['name'],
                'description': repo.get('description') or '',
                'language': repo.get('language') or '',
                'stars': repo.get('stargazers_count', 0),
                'forks': repo.get('forks_count', 0),
                'updated_at': repo.get('updated_at'),
                'url': repo.get('html_url'),
            }
            for repo in repos_response.json()
        ]
        languages = {}
        for repo in repositories:
            if repo['language']:
                languages[repo['language']] = languages.get(repo['language'], 0) + 1
        return Response({
            'success': True,
            'profile': profile_data,
            'repositories': repositories,
            'languages': languages,
            'total_stars': sum(repo['stars'] for repo in repositories),
        })
    except (requests.RequestException, ValueError, KeyError):
        return Response({
            'success': True,
            'profile': {
                'username': username,
                'name': 'Dhanaraj Lokhande',
                'bio': 'AI/ML Engineer | Data Scientist',
                'html_url': f'https://github.com/{username}',
            },
            'repositories': [],
            'languages': {},
            'total_stars': 0,
        })


@api_view(['GET'])
def api_overview(request):
    """API root — list available endpoints."""
    return Response({
        'profile': '/api/profile/',
        'education': '/api/education/',
        'experience': '/api/experience/',
        'projects': '/api/projects/',
        'skills': '/api/skills/',
        'certifications': '/api/certifications/',
        'activities': '/api/activities/',
        'achievements': '/api/achievements/',
        'social_links': '/api/social-links/',
        'job_roles': '/api/job-roles/',
        'contact': '/api/contact/',
    })


@api_view(['GET'])
def profile_api(request):
    p = content.PROFILE
    return Response({
        'full_name': p.full_name,
        'title': p.title,
        'bio': p.bio,
        'location': p.location,
        'email': p.email,
        'phone': p.phone,
        'photo_url': p.photo.url or None,
        'resume_url': p.resume_pdf.url or None,
        'professional_summary': p.professional_summary,
    })


@api_view(['GET'])
def education_api(request):
    return Response([
        {
            'degree': e.degree, 'level': e.level, 'institution': e.institution,
            'university': e.university, 'start_year': e.start_year,
            'end_year': e.end_year, 'cgpa': e.cgpa, 'percentage': e.percentage,
            'description': e.description, 'score_display': e.score_display,
        }
        for e in content.EDUCATION
    ])


@api_view(['GET'])
def experience_api(request):
    return Response([
        {
            'title': e.title, 'company': e.company, 'location': e.location,
            'start_date': e.start_date, 'end_date': e.end_date,
            'is_current': e.is_current, 'description': e.description,
            'responsibilities_list': e.responsibilities_list,
            'duration_display': e.duration_display,
        }
        for e in content.EXPERIENCE
    ])


def _project_card(p):
    return {
        'title': p.title, 'slug': p.slug, 'short_description': p.short_description,
        'algorithm': p.algorithm, 'github_url': p.github_url,
        'live_demo_url': p.live_demo_url, 'is_featured': p.is_featured,
        'order': p.order, 'features_list': p.features_list,
        'technologies': [{'name': t.name} for t in p.technologies.all()],
    }


@api_view(['GET'])
def projects_api(request):
    return Response([_project_card(p) for p in content.PROJECTS])


@api_view(['GET'])
def project_detail_api(request, slug):
    project = next((p for p in content.PROJECTS if p.slug == slug), None)
    if project is None:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    data = _project_card(project)
    data.update({
        'description': project.description,
        'problem_statement': project.problem_statement,
        'solution': project.solution,
        'architecture': project.architecture,
        'features': project.features,
        'dataset_info': project.dataset_info,
        'results': project.results,
        'challenges': project.challenges,
        'future_improvements': project.future_improvements,
        'workflow_steps': [
            {'title': s.title, 'description': s.description, 'icon': s.icon, 'order': s.order}
            for s in project.workflow_steps.all()
        ],
    })
    return Response(data)


@api_view(['GET'])
def skills_api(request):
    return Response([
        {
            'name': s.name, 'category': s.category,
            'category_display': s.category_display,
            'proficiency': s.proficiency, 'icon': s.icon,
        }
        for s in content.SKILLS
    ])


@api_view(['GET'])
def certifications_api(request):
    return Response([
        {
            'title': c.title, 'organization': c.organization,
            'description': c.description, 'skills_list': c.skills_list,
            'verification_url': c.verification_url, 'date_earned': c.date_earned,
        }
        for c in content.CERTIFICATIONS
    ])


@api_view(['GET'])
def activities_api(request):
    return Response([
        {
            'title': a.title, 'category': a.category,
            'category_display': a.category_display,
            'description': a.description, 'date': a.date, 'icon': a.icon,
        }
        for a in content.ACTIVITIES
    ])


@api_view(['GET'])
def achievements_api(request):
    return Response([
        {'title': a.title, 'description': a.description, 'date': a.date, 'icon': a.icon}
        for a in content.ACHIEVEMENTS
    ])


@api_view(['GET'])
def social_links_api(request):
    return Response([
        {
            'platform': s.platform, 'platform_display': s.platform_display,
            'url': s.url, 'display_name': s.display_name, 'icon_class': s.icon_class,
        }
        for s in content.SOCIAL_LINKS
    ])


@api_view(['GET'])
def job_roles_api(request):
    return Response([{'title': j.title} for j in content.JOB_ROLES])


@api_view(['POST'])
def contact_api(request):
    """Contact submissions are not stored (no database)."""
    return Response(
        {'success': True, 'message': 'Please email lokhandedhanraj2410@gmail.com directly.'},
        status=status.HTTP_200_OK,
    )
