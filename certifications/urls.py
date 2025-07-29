from django.urls import path
from . import views
urlpatterns=[
    path('my-certifications/', views.certifications, name='certifications'),
]