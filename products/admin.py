from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_id',
        'name',
        'description',
        'price',
        'image',
    )

    ordering =('product_id',)

admin.site.register(Product, ProductAdmin) 