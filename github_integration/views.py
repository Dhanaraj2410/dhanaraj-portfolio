"""
GitHub integration API views.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import get_github_data


@api_view(['GET'])
def github_api(request):
    """
    GET /api/github/
    Returns GitHub profile and repository data (cached).
    """
    data = get_github_data()
    return Response(data)
