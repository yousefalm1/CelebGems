from django.contrib import admin
from .models import CelebRequest, CelebProfile

# Register your models here.

@admin.register(CelebRequest)
class CelebRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'occupation', 'approved']
    list_filter = ['approved']
    search_fields = ['user__username', 'occupation']
    list_per_page = 20