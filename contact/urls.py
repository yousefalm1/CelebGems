from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.contact_page,
        name='contact'
    ),

    path(
        'contact/success/',
        views.contact_us_success,
        name='contact_us_success'
    ),
]
