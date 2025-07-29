from django.urls import path
from . import views
urlpatterns=[
    path('my-resume/', views.resume, name='resume'),
]