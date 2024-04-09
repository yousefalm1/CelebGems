from django.contrib import admin
from .models import CelebRequest, CelebProfile

@admin.register(CelebRequest)
class CelebRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'occupation', 'approved']
    list_filter = ['approved']
    search_fields = ['user__username', 'occupation']
    list_per_page = 20

@admin.register(CelebProfile)
class CelebProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_name', 'bio')  # Specify which fields to display in the list view
    search_fields = ('user__username', 'profile_name')