from django.urls import path
from .views import request_celeb_profile_page, request_celeb_profile_submitted, request_already_submitted, celeb_profile_page, create_celeb_profile_page, edit_celeb_profile, edit_celeb_profile_confirmation, add_product, edit_product, edit_product_success, delete_product, add_product_success, celeb_profile

urlpatterns = [

    path('request-celeb-profile/',request_celeb_profile_page, name='request_celeb_profile_page'),
    path('request-celeb-profile/submitted/',request_celeb_profile_submitted, name='request_celeb_profile_submitted'),
    path('request-celeb-profile/already-submitted/', request_already_submitted, name='request_already_submitted'),


    path('view-profile/<int:user_id>/', celeb_profile, name='celeb_profile'),

    # Celeb Profile Main Page
    path('celeb-profile/', celeb_profile_page, name='celeb_profile_page'),

    # Create Celeb Profile
    path('create-celeb-profile/', create_celeb_profile_page, name='create_celeb_profile_page'),

    # Edit Celeb Profile
    path('edit-celeb-profile/', edit_celeb_profile, name='edit_celeb_profile'),
    path('edit-celeb-profile/confirmation', edit_celeb_profile_confirmation, name='edit_celeb_profile_confirmation'),

    # Celeb Add Product
    path('add-product/', add_product, name='add_product'),
    path('add-product/success', add_product_success, name='add_product_success'),

    # Celeb Edit Product
    path('edit-product/<int:product_id>/', edit_product, name='edit_product'),
    path('edit-product/success/<int:product_id>/', edit_product_success, name='edit_product_success'),

    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    
]