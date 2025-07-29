from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'live_link', 'created_at', 'updated_at']

