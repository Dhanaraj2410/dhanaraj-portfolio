"""
Django models for the AI/ML Portfolio platform.
All content is managed through Django Admin — no hardcoded data.
"""
from django.db import models
from django.utils import timezone


class SingletonModel(models.Model):
    """Base class for models that should only have one instance."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    """Global site configuration — singleton."""
    site_title = models.CharField(max_length=200, default='Dhanaraj AI/ML Portfolio')
    tagline = models.CharField(max_length=300, default='AI/ML Engineer | Data Scientist | Python Developer | Data Analyst')
    secondary_tagline = models.CharField(
        max_length=500,
        default='My Skills, Projects, Experience, Certifications & Career Journey — All in One Place.',
    )
    github_username = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(blank=True)
    meta_description = models.TextField(
        default='Dhanaraj Arjun Lokhande — AI/ML Engineer & Data Scientist portfolio showcasing Python, Machine Learning, and Data Science projects.',
        max_length=300,
    )

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_title


class Profile(models.Model):
    """Main profile / candidate information."""
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, help_text='e.g. AI/ML Engineer | Data Scientist')
    bio = models.TextField(help_text='Professional summary / about description')
    location = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_pdf = models.FileField(upload_to='resume/', blank=True, null=True)
    professional_summary = models.TextField(
        blank=True,
        help_text='Detailed professional summary for the resume section',
    )

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.full_name


class Education(models.Model):
    """Educational qualifications."""
    LEVEL_CHOICES = [
        ('BE', 'Bachelor of Engineering'),
        ('BSC', 'Bachelor of Science'),
        ('MSC', 'Master of Science'),
        ('ME', 'Master of Engineering'),
        ('HSC', 'Higher Secondary Certificate'),
        ('SSC', 'Secondary School Certificate'),
        ('OTHER', 'Other'),
    ]

    degree = models.CharField(max_length=200, help_text='e.g. Bachelor of Engineering – Information Technology')
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='OTHER')
    institution = models.CharField(max_length=300)
    university = models.CharField(max_length=300, blank=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0, help_text='Display order (lower = first)')

    class Meta:
        ordering = ['order', '-end_year']
        verbose_name_plural = 'Education'

    def __str__(self):
        return f"{self.degree} — {self.institution}"

    @property
    def score_display(self):
        if self.cgpa:
            return f"CGPA: {self.cgpa}"
        elif self.percentage:
            return f"{self.percentage}%"
        return ""


class Experience(models.Model):
    """Work experience / internships."""
    title = models.CharField(max_length=200, help_text='e.g. Data Science Intern')
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text='Leave blank if current')
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True, help_text='General description of the role')
    responsibilities = models.TextField(
        blank=True,
        help_text='One responsibility per line',
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f"{self.title} at {self.company}"

    @property
    def responsibilities_list(self):
        if not self.responsibilities:
            return []
        return [r.strip() for r in self.responsibilities.strip().split('\n') if r.strip()]

    @property
    def duration_display(self):
        start = self.start_date.strftime('%m/%Y')
        if self.is_current or not self.end_date:
            return f"{start} – Present"
        return f"{start} – {self.end_date.strftime('%m/%Y')}"


class Project(models.Model):
    """Portfolio projects."""
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    short_description = models.TextField(help_text='Brief description for project cards')
    description = models.TextField(help_text='Full project description')
    problem_statement = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    architecture = models.TextField(blank=True)
    features = models.TextField(blank=True, help_text='One feature per line')
    algorithm = models.CharField(max_length=200, blank=True, help_text='e.g. Logistic Regression')
    dataset_info = models.TextField(blank=True, help_text='Dataset description')
    results = models.TextField(blank=True, help_text='Results, accuracy, metrics')
    challenges = models.TextField(blank=True)
    future_improvements = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    screenshot = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def features_list(self):
        if not self.features:
            return []
        return [f.strip() for f in self.features.strip().split('\n') if f.strip()]


class ProjectTechnology(models.Model):
    """Technologies used in a project (many-to-one)."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Project Technology'
        verbose_name_plural = 'Project Technologies'

    def __str__(self):
        return f"{self.name} ({self.project.title})"


class ProjectWorkflowStep(models.Model):
    """Workflow steps for project visualization."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='workflow_steps')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text='CSS icon class or emoji')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Workflow Step'

    def __str__(self):
        return f"Step {self.order}: {self.title}"


class Skill(models.Model):
    """Technical and soft skills."""
    CATEGORY_CHOICES = [
        ('PROGRAMMING', 'Programming'),
        ('LIBRARIES', 'Python Libraries'),
        ('ML', 'Machine Learning'),
        ('VISUALIZATION', 'Visualization'),
        ('TOOLS', 'Developer Tools'),
        ('SOFT', 'Soft Skills'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(
        default=70,
        help_text='Proficiency level 1-100 (self-assessed, not a certification)',
    )
    icon = models.CharField(max_length=50, blank=True, help_text='CSS icon class or emoji')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Certification(models.Model):
    """Professional certifications and courses."""
    title = models.CharField(max_length=300)
    organization = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    skills = models.TextField(blank=True, help_text='Key skills covered, one per line')
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    certificate_pdf = models.FileField(upload_to='certificates/', blank=True, null=True)
    verification_url = models.URLField(blank=True, help_text='Official verification link (if available)')
    date_earned = models.DateField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} — {self.organization}"

    @property
    def skills_list(self):
        if not self.skills:
            return []
        return [s.strip() for s in self.skills.strip().split('\n') if s.strip()]


class Activity(models.Model):
    """Career activities for the activity dashboard."""
    CATEGORY_CHOICES = [
        ('CODING', 'Coding Activity'),
        ('LEARNING', 'Learning Activity'),
        ('CAREER', 'Career Activity'),
    ]

    title = models.CharField(max_length=300)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    icon = models.CharField(max_length=50, blank=True, default='📌')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-date']
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"


class Achievement(models.Model):
    """Notable achievements and awards."""
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, default='🏆')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-date']

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    """Social media and professional links."""
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('email', 'Email'),
        ('twitter', 'Twitter/X'),
        ('portfolio', 'Portfolio'),
        ('kaggle', 'Kaggle'),
        ('other', 'Other'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.CharField(max_length=500, help_text='URL or email address')
    display_name = models.CharField(max_length=200, blank=True)
    icon_class = models.CharField(max_length=100, blank=True, help_text='CSS icon class')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Social Link'

    def __str__(self):
        return f"{self.get_platform_display()}: {self.url}"


class ContactMessage(models.Model):
    """Messages received from the contact form."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True)
    job_role = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'

    def __str__(self):
        return f"Message from {self.name} ({self.email}) — {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class GitHubCache(models.Model):
    """Cached GitHub API data to reduce API calls."""
    data = models.JSONField(default=dict)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'GitHub Cache'
        verbose_name_plural = 'GitHub Cache'

    def __str__(self):
        return f"GitHub Cache (updated {self.updated_at})"

    @property
    def is_stale(self):
        """Cache is stale after 1 hour."""
        if not self.updated_at:
            return True
        return (timezone.now() - self.updated_at).total_seconds() > 3600


class JobRole(models.Model):
    """Recommended job roles for the recruiter dashboard."""
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Recommended Job Role'

    def __str__(self):
        return self.title


class RoleResume(models.Model):
    """Role-specific resume files and summaries for targeted 2026 Fresher applications."""
    ROLE_CHOICES = [
        ('data-analyst', 'Data Analyst / Business Analyst'),
        ('data-science', 'Data Science / Data Scientist'),
        ('machine-learning', 'Machine Learning / AI Engineer'),
        ('python-developer', 'Python Developer'),
        ('sql-developer', 'SQL Developer / Database Analyst'),
    ]

    role_key = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(help_text='Tailored professional summary for this role')
    key_skills = models.TextField(help_text='Comma-separated skills')
    resume_file = models.FileField(upload_to='resumes/roles/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Role Specific Resume'
        verbose_name_plural = 'Role Specific Resumes'

    def __str__(self):
        return f"{self.get_role_key_display()} Resume"

