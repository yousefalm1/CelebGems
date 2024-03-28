from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    # specifies the fields in the admin interface that should be displayed as read-only,
    readonly_fields = ('order_number', 'data', 'delivery_cost', 'order_total', 'grand_total',)

    # specifies the order in which the fields should appear in the admin interface
    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county', 'delivery_cost', 'order_total','grand_total',)

    # specifies which fields should be displayed as columns in the list view of orders in the admin interface
    list_display = ('order_number', 'date', 'full_name','order_total', 'delivery_cost',  'grand_total',)

    ordering = ('-date',)