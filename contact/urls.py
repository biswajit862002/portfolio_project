# from django.urls import path
# from . import views

# urlpatterns=[
#     path('contact-me/', views.contact, name='contact'),

# ]


from django.urls import path
from .views import contact_view

urlpatterns = [
    path('contact-me/', contact_view, name='contact'),
]
