from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'price', 'display_on_home', 'celeb_profile')
    ordering = ('product_id',)
admin.site.register(Product, ProductAdmin) 