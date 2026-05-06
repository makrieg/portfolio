from django.db import models
from django.urls import reverse


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web App'),
        ('data', 'Data/ML'),
        ('tool', 'Tool/Library'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    tools_used = models.CharField(max_length=500, blank=True, help_text='Comma-separated list of tools/technologies')
    challenges = models.TextField(blank=True)
    lessons_learned = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    additional_links = models.TextField(blank=True, help_text='Optional: JSON array or comma-separated URLs')

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

    def get_tools_list(self):
        return [t.strip() for t in self.tools_used.split(',')] if self.tools_used else []

    def get_links_list(self):
        if not self.additional_links:
            return []
        # try JSON-like list first, otherwise comma-separated
        text = self.additional_links.strip()
        if text.startswith('[') and text.endswith(']'):
            try:
                import json

                return json.loads(text)
            except Exception:
                pass
        return [l.strip() for l in text.split(',') if l.strip()]


class PortfolioSkill(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=120)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate')
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    details = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-start_date', 'order']

    def __str__(self):
        return f"{self.title} @ {self.company}" if self.company else self.title
