from django.contrib import admin
from .models import Project, PortfolioSkill, Experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'created_at')
    list_filter = ('category', 'featured')
    search_fields = ('title', 'summary', 'description', 'tools_used')


@admin.register(PortfolioSkill)
class PortfolioSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'order')
    list_filter = ('proficiency',)
    search_fields = ('name',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'currently')
    list_filter = ('currently',)
    search_fields = ('title', 'company')
