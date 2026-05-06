from django.contrib import admin
from .models import Skill, Review, BookingRequest


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'price', 'availability', 'created_at')
    list_filter = ('category', 'availability', 'is_free')
    search_fields = ('title', 'description', 'owner__username')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('skill', 'reviewer', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('skill__title', 'reviewer__username', 'comment')


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('skill', 'requester', 'status', 'preferred_date', 'created_at')
    list_filter = ('status', 'created_at', 'preferred_date')
    search_fields = ('skill__title', 'requester__username', 'message')
    readonly_fields = ('created_at', 'updated_at')
