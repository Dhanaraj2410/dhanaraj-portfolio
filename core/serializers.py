"""
DRF Serializers for the portfolio API.
"""
from rest_framework import serializers
from .models import (
    SiteSettings, Profile, Education, Experience, Project,
    ProjectTechnology, ProjectWorkflowStep, Skill, Certification,
    Activity, Achievement, SocialLink, ContactMessage, JobRole,
)


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    resume_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'full_name', 'title', 'bio', 'location',
            'email', 'phone', 'photo_url', 'resume_url',
            'professional_summary',
        ]

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None

    def get_resume_url(self, obj):
        if obj.resume_pdf:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.resume_pdf.url)
            return obj.resume_pdf.url
        return None


class EducationSerializer(serializers.ModelSerializer):
    score_display = serializers.ReadOnlyField()

    class Meta:
        model = Education
        fields = [
            'id', 'degree', 'level', 'institution', 'university',
            'start_year', 'end_year', 'cgpa', 'percentage',
            'description', 'score_display',
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    responsibilities_list = serializers.ReadOnlyField()
    duration_display = serializers.ReadOnlyField()

    class Meta:
        model = Experience
        fields = [
            'id', 'title', 'company', 'location', 'start_date',
            'end_date', 'is_current', 'description',
            'responsibilities_list', 'duration_display',
        ]


class ProjectTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTechnology
        fields = ['id', 'name']


class ProjectWorkflowStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectWorkflowStep
        fields = ['id', 'title', 'description', 'icon', 'order']


class ProjectListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for project list views."""
    technologies = ProjectTechnologySerializer(many=True, read_only=True)
    features_list = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'short_description', 'algorithm',
            'github_url', 'live_demo_url', 'is_featured', 'technologies',
            'features_list',
        ]


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Full serializer for project detail views."""
    technologies = ProjectTechnologySerializer(many=True, read_only=True)
    workflow_steps = ProjectWorkflowStepSerializer(many=True, read_only=True)
    features_list = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'short_description', 'description',
            'problem_statement', 'solution', 'architecture', 'features',
            'features_list', 'algorithm', 'dataset_info', 'results',
            'challenges', 'future_improvements', 'github_url',
            'live_demo_url', 'is_featured', 'technologies', 'workflow_steps',
        ]


class SkillSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'category_display', 'proficiency', 'icon']


class CertificationSerializer(serializers.ModelSerializer):
    skills_list = serializers.ReadOnlyField()

    class Meta:
        model = Certification
        fields = [
            'id', 'title', 'organization', 'description', 'skills_list',
            'verification_url', 'date_earned',
        ]


class ActivitySerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'title', 'category', 'category_display', 'description', 'date', 'icon']


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'title', 'description', 'date', 'icon']


class SocialLinkSerializer(serializers.ModelSerializer):
    platform_display = serializers.CharField(source='get_platform_display', read_only=True)

    class Meta:
        model = SocialLink
        fields = ['id', 'platform', 'platform_display', 'url', 'display_name', 'icon_class']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'company', 'job_role', 'message']

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Message must be at least 10 characters long.")
        return value


class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRole
        fields = ['id', 'title']
