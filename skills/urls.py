from django.urls import path
from . import views
urlpatterns=[
 path('my-skills/', views.skills, name='skills')
]