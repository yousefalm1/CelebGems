from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/', views.add_bag, name='add_bag'),
    path('delete/', views.delete_bag, name='delete_bag'),
    path('update/', views.update_bag, name='update_bag'),

] 