"""
URL routing for the core portfolio app.
"""
from django.urls import path
from . import views, api_views

app_name = 'core'

urlpatterns = [
    # ─── Template Views ────────────────────────────────────────────────
    path('', views.home, name='home'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('robots.txt', views.robots_txt, name='robots_txt'),

    # ─── REST API ──────────────────────────────────────────────────────
    path('api/', api_views.api_overview, name='api_overview'),
    path('api/profile/', api_views.profile_api, name='api_profile'),
    path('api/education/', api_views.EducationListAPI.as_view(), name='api_education'),
    path('api/experience/', api_views.ExperienceListAPI.as_view(), name='api_experience'),
    path('api/projects/', api_views.ProjectListAPI.as_view(), name='api_projects'),
    path('api/projects/<slug:slug>/', api_views.ProjectDetailAPI.as_view(), name='api_project_detail'),
    path('api/skills/', api_views.SkillListAPI.as_view(), name='api_skills'),
    path('api/certifications/', api_views.CertificationListAPI.as_view(), name='api_certifications'),
    path('api/activities/', api_views.ActivityListAPI.as_view(), name='api_activities'),
    path('api/achievements/', api_views.AchievementListAPI.as_view(), name='api_achievements'),
    path('api/social-links/', api_views.SocialLinkListAPI.as_view(), name='api_social_links'),
    path('api/job-roles/', api_views.JobRoleListAPI.as_view(), name='api_job_roles'),
    path('api/contact/', api_views.contact_api, name='api_contact'),
]
