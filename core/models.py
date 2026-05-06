from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES)
    category = models.CharField(
        max_length=50,
        choices=[
            ('language', 'Programming Language'),
            ('framework', 'Framework'),
            ('tool', 'Tool'),
            ('other', 'Other'),
        ],
        default='tool'
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    business_problem = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    learning_objectives = models.TextField(blank=True)
    project_requirements = models.TextField(blank=True)
    key_features = models.TextField(blank=True)
    role_contribution = models.TextField(blank=True)
    biggest_challenge = models.TextField(blank=True)
    what_learned = models.TextField(blank=True)
    included_files = models.TextField(blank=True, help_text="One file or asset per line")
    information_needed = models.TextField(blank=True, help_text="Use this space for any missing details still needed")
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]


class ProjectAsset(models.Model):
    ASSET_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
        ('other', 'Other'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='assets')
    title = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES, default='other')
    file = models.FileField(upload_to='projects/assets/', blank=True, null=True)
    external_url = models.URLField(blank=True)
    caption = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.project.title} - {self.title}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
