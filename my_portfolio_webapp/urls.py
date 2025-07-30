"""
URL configuration for my_portfolio_webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home, name='home'),
    path("resume/",include('my_resume.urls')),
    path("skill/",include('skills.urls')),
    path("project/",include('my_projects.urls')),
    path("social-links/",include('social_links.urls')),
    path("certificates/",include('certifications.urls')),
    path("blogs/",include('blogs.urls')),
    path("contact/",include('contact.urls')),

] 

# Serve media only if in DEBUG mode or fallback
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # ✅ Force serve media manually (safe for small projects)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
