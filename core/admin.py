from django.contrib import admin
from .models import Project, ProjectAsset, Skill, Contact


class ProjectAssetInline(admin.TabularInline):
    model = ProjectAsset
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('title', 'description', 'overview', 'information_needed')
    ordering = ('-featured', '-created_at')
    inlines = [ProjectAssetInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'technologies', 'project_url', 'github_url', 'featured', 'order')
        }),
        ('Assignment Sections', {
            'fields': (
                'business_problem',
                'key_features',
                'role_contribution',
                'biggest_challenge',
                'what_learned',
                'overview',
                'learning_objectives',
                'project_requirements',
                'included_files',
                'information_needed',
            )
        }),
    )


@admin.register(ProjectAsset)
class ProjectAssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'asset_type', 'order')
    list_filter = ('asset_type',)
    search_fields = ('title', 'caption', 'project__title')
    ordering = ('project', 'order', 'title')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)
    ordering = ('order', 'name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'read')
    list_filter = ('read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
