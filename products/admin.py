from django.contrib import admin
from .models import Product

# Register your models here.


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