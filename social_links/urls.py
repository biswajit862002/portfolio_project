from django.urls import path
from . import views
urlpatterns=[
 path('all-links/', views.social, name='social')
]