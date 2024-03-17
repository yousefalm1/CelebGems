from django.urls import path
from .views import request_celeb_profile_page, request_celeb_profile_submitted, request_already_submitted, celeb_profile_page, create_celeb_profile_page, edit_celeb_profile, edit_celeb_profile_confirmation

urlpatterns = [
    path('request-celeb-profile/',request_celeb_profile_page, name='request_celeb_profile_page'),
    path('request-celeb-profile/submitted/',request_celeb_profile_submitted, name='request_celeb_profile_submitted'),
    path('request-celeb-profile/already-submitted/', request_already_submitted, name='request_already_submitted'),
    path('celeb-profile/', celeb_profile_page, name='celeb_profile_page'),
    path('create-celeb-profile/', create_celeb_profile_page, name='create_celeb_profile_page'),
    path('edit-celeb-profile/', edit_celeb_profile, name='edit_celeb_profile'),
    path('edit-celeb-profile/confirmation', edit_celeb_profile_confirmation, name='edit_celeb_profile_confirmation'),
    


    
]