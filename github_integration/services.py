"""
GitHub API integration service.
Fetches public repository data with caching.
"""
import logging
import requests
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)

GITHUB_API_BASE = 'https://api.github.com'


def get_github_data():
    """
    Fetch GitHub profile and repository data.
    Uses 1-hour cache to respect API rate limits.
    Returns cached data if available and fresh.
    """
    from core.models import GitHubCache, SiteSettings

    username = getattr(settings, 'GITHUB_USERNAME', '')
    if not username:
        try:
            site = SiteSettings.load()
            username = site.github_username
        except Exception:
            pass
    if not username:
        username = 'Dhanaraj2410'


    # Check cache
    cache = GitHubCache.objects.first()
    if cache and not cache.is_stale and cache.data:
        return {'success': True, 'cached': True, **cache.data}

    # Fetch fresh data
    try:
        data = _fetch_github_data(username)
        if data:
            if cache:
                cache.data = data
                cache.save()
            else:
                GitHubCache.objects.create(data=data)
            return {'success': True, 'cached': False, **data}
        return {'success': False, 'error': 'Could not fetch GitHub data.'}
    except Exception as e:
        logger.error(f"GitHub API error: {e}")
        # Return stale cache if available
        if cache and cache.data:
            return {'success': True, 'cached': True, 'stale': True, **cache.data}
        return {'success': False, 'error': 'GitHub API unavailable.'}


def _fetch_github_data(username):
    """Fetch data from GitHub API."""
    headers = {'Accept': 'application/vnd.github.v3+json'}
    token = settings.GITHUB_TOKEN
    if token:
        headers['Authorization'] = f'token {token}'

    # Fetch user profile
    user_resp = requests.get(
        f'{GITHUB_API_BASE}/users/{username}',
        headers=headers,
        timeout=10,
    )

    if user_resp.status_code != 200:
        logger.warning(f"GitHub user API returned {user_resp.status_code}")
        return None

    user_data = user_resp.json()

    # Fetch repositories
    repos_resp = requests.get(
        f'{GITHUB_API_BASE}/users/{username}/repos',
        headers=headers,
        params={'sort': 'updated', 'per_page': 30, 'type': 'owner'},
        timeout=10,
    )

    repos = []
    languages = {}
    total_stars = 0

    if repos_resp.status_code == 200:
        for repo in repos_resp.json():
            repo_info = {
                'name': repo['name'],
                'description': repo.get('description', ''),
                'language': repo.get('language', ''),
                'stars': repo.get('stargazers_count', 0),
                'forks': repo.get('forks_count', 0),
                'url': repo.get('html_url', ''),
                'updated_at': repo.get('updated_at', ''),
                'topics': repo.get('topics', []),
            }
            repos.append(repo_info)
            total_stars += repo_info['stars']

            lang = repo.get('language')
            if lang:
                languages[lang] = languages.get(lang, 0) + 1

    return {
        'profile': {
            'username': user_data.get('login', username),
            'name': user_data.get('name', ''),
            'bio': user_data.get('bio', ''),
            'avatar_url': user_data.get('avatar_url', ''),
            'html_url': user_data.get('html_url', f'https://github.com/{username}'),
            'public_repos': user_data.get('public_repos', 0),
            'followers': user_data.get('followers', 0),
            'following': user_data.get('following', 0),
        },
        'repositories': repos,
        'total_stars': total_stars,
        'languages': languages,
        'fetched_at': timezone.now().isoformat(),
    }
