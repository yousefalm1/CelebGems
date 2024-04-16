from django.contrib import admin
from .models import contactMessage


@admin.register
class contactMessageAdmin(admin.ModelAdmin):
    list_display = ('Name', 'email', 'subject')
    search_fields = ('Name', 'email', 'subject')
