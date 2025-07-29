from django.urls import path
from . import views
urlpatterns=[
    path('my-projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
]