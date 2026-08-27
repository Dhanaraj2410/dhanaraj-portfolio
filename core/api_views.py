"""
REST API views for the portfolio platform.
"""
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Profile, Education, Experience, Project,
    Skill, Certification, Activity, Achievement,
    SocialLink, JobRole, SiteSettings,
)
from .serializers import (
    ProfileSerializer, EducationSerializer, ExperienceSerializer,
    ProjectListSerializer, ProjectDetailSerializer, SkillSerializer,
    CertificationSerializer, ActivitySerializer, AchievementSerializer,
    SocialLinkSerializer, ContactMessageSerializer, JobRoleSerializer,
    SiteSettingsSerializer,
)


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
        'ai_chat': '/api/ai/chat/',
        'ai_resume_analysis': '/api/ai/resume-analysis/',
        'github': '/api/github/',
    })


@api_view(['GET'])
def profile_api(request):
    """Get the main profile."""
    profile = Profile.objects.first()
    if not profile:
        return Response({'detail': 'Profile not configured.'}, status=404)
    serializer = ProfileSerializer(profile, context={'request': request})
    return Response(serializer.data)


class EducationListAPI(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    pagination_class = None


class ExperienceListAPI(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    pagination_class = None


class ProjectListAPI(generics.ListAPIView):
    queryset = Project.objects.prefetch_related('technologies').all()
    serializer_class = ProjectListSerializer
    pagination_class = None


class ProjectDetailAPI(generics.RetrieveAPIView):
    queryset = Project.objects.prefetch_related('technologies', 'workflow_steps').all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'slug'


class SkillListAPI(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    pagination_class = None


class CertificationListAPI(generics.ListAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    pagination_class = None


class ActivityListAPI(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = None


class AchievementListAPI(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None


class SocialLinkListAPI(generics.ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    pagination_class = None


class JobRoleListAPI(generics.ListAPIView):
    queryset = JobRole.objects.all()
    serializer_class = JobRoleSerializer
    pagination_class = None


@api_view(['POST'])
def contact_api(request):
    """Handle contact form submission via API."""
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'success': True, 'message': 'Thank you for your message!'},
            status=status.HTTP_201_CREATED,
        )
    return Response(
        {'success': False, 'errors': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )
