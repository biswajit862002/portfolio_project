from django.urls import path
from . import views
urlpatterns=[
    path('my-blogs/', views.blogs, name='blogs'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('test-upload/', views.test_upload, name='test_upload'),

]