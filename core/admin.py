"""
Django Admin configuration for the portfolio platform.
Rich admin interface for managing all portfolio content.
"""
from django.contrib import admin
from django.utils.html import mark_safe
from .models import (
    SiteSettings, Profile, Education, Experience, Project,
    ProjectTechnology, ProjectWorkflowStep, Skill, Certification,
    Activity, Achievement, SocialLink, ContactMessage, GitHubCache,
    JobRole, RoleResume,
)


# ─── Inlines ──────────────────────────────────────────────────────────────────

class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 2
    ordering = ['order']


class ProjectWorkflowStepInline(admin.TabularInline):
    model = ProjectWorkflowStep
    extra = 3
    ordering = ['order']


# ─── Admin Classes ────────────────────────────────────────────────────────────

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Site Identity', {
            'fields': ('site_title', 'tagline', 'secondary_tagline'),
        }),
        ('External Links', {
            'fields': ('github_username', 'linkedin_url'),
        }),
        ('SEO', {
            'fields': ('meta_description',),
        }),
    )

    def has_add_permission(self, request):
        # Only one instance allowed
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'email', 'location']
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'title', 'photo'),
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'location'),
        }),
        ('Bio & Summary', {
            'fields': ('bio', 'professional_summary'),
        }),
        ('Resume', {
            'fields': ('resume_pdf',),
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'end_year', 'score_display', 'order']
    list_editable = ['order']
    list_filter = ['level']
    ordering = ['order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'order']
    list_editable = ['order', 'is_current']
    list_filter = ['is_current']
    ordering = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'algorithm', 'is_featured', 'order']
    list_editable = ['is_featured', 'order']
    list_filter = ['is_featured']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description']
    inlines = [ProjectTechnologyInline, ProjectWorkflowStepInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'description', 'screenshot'),
        }),
        ('Project Details', {
            'fields': ('problem_statement', 'solution', 'architecture', 'features'),
        }),
        ('ML/AI Details', {
            'fields': ('algorithm', 'dataset_info', 'results'),
        }),
        ('Reflection', {
            'fields': ('challenges', 'future_improvements'),
        }),
        ('Links', {
            'fields': ('github_url', 'live_demo_url'),
        }),
        ('Display', {
            'fields': ('is_featured', 'order'),
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['proficiency', 'order']
    list_filter = ['category']
    ordering = ['category', 'order']
    search_fields = ['name']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'image_preview', 'date_earned', 'order']
    list_editable = ['order']
    readonly_fields = ['image_preview']
    ordering = ['order']
    fieldsets = (
        ('Certification Details', {
            'fields': ('title', 'organization', 'description', 'skills', 'date_earned'),
        }),
        ('Certificate Image & PDF Uploads', {
            'fields': ('certificate_image', 'image_preview', 'certificate_pdf'),
            'description': 'Upload your certificate image (JPG/PNG) or PDF document here.',
        }),
        ('Verification', {
            'fields': ('verification_url',),
        }),
        ('Display Order', {
            'fields': ('order',),
        }),
    )

    def image_preview(self, obj):
        if obj.certificate_image:
            return mark_safe(f'<img src="{obj.certificate_image.url}" style="max-height: 70px; max-width: 110px; border-radius: 4px; border: 1px solid #ccc;" />')
        return mark_safe('<span style="color: #999;">No Image</span>')
    image_preview.short_description = "Certificate Preview"


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date', 'order']
    list_editable = ['order']
    list_filter = ['category']
    ordering = ['order', '-date']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'display_name', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'job_role', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at']
    readonly_fields = ['name', 'email', 'company', 'job_role', 'message', 'created_at']
    ordering = ['-created_at']

    def has_add_permission(self, request):
        return False


@admin.register(GitHubCache)
class GitHubCacheAdmin(admin.ModelAdmin):
    list_display = ['updated_at', 'is_stale']
    readonly_fields = ['data', 'updated_at']

    def has_add_permission(self, request):
        return False


@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(RoleResume)
class RoleResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'role_key', 'resume_file', 'order']
    list_editable = ['order']
    ordering = ['order']

