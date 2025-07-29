from django.contrib import admin
from .models import Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'technology', 'image', 'live_link', 'github_link', 'start_date', 'end_date', 'created_at', 'updated_at']


