from django.contrib import admin
from .models import Blogs
from django.utils.html import format_html

# Register your models here.

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'technology', 'image', 'github_link', 'start_date', 'end_date', 'created_at', 'updated_at']



