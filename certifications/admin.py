from django.contrib import admin
from .models import Certification

# Register your models here.
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'live_link', 'organization_name', 'issue_date', 'created_at', 'updated_at']

