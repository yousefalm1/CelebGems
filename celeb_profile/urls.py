from django.urls import path
from .views import request_celeb_profile_page, request_celeb_profile_submitted

urlpatterns = [
    path('request-celeb-profile/',request_celeb_profile_page, name='request_celeb_profile_page'),
    path('request-celeb-profile/submitted',request_celeb_profile_submitted, name='request_celeb_profile_submitted'),
    
]