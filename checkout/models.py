# Generate a order number
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product   
from profiles.models import UserProfile
# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


    def _generate_order_number(self):
        """ Generate a random order number using uuid """

        # generate a random string of 32 characters
        return uuid.uuid4().hex.upper()
    


    def update_total(self):
        """
        Update grand total each time a line is added
        """
        # Takes all the lineitems(Orders) in the OrderLineItem and aggregates to sum up all the lineitem_total field cross all line items related to the current order instance 
        # The adds a new filed to the query set called lineitem_total__sum which we can get and set the order total to that 
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']

        # Checks if the order total is below the free delivery threshold
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            # Calculate delivery cost based on order total and STANDARD_DELIVERY_PERCENTAGE
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            # set delivery cost to 0 if order qualifies for free delivery
            self.delivery_cost = 0 
        
        # Calculate grand total by adding order_total and delivery_cost
        self.grand_total = self.order_total + self.delivery_cost

        # Save the updated order instance
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the default save method to set the order number if it hasn't been set already.
        """
        # Checks if the order number attribute of the current instance of the model is not set or empty if so 
        # it generates a order number
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# Stores each order in a lime 
class OrderLineItem(models.Model):
    Order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name="lineitems")
    product = models.ForeignKey(Product, null= False, blank= False, on_delete=models.CASCADE )
    product_size = models.CharField(max_length=2, null=True, blank= True ) #XS, S, M,
    quantity = models.IntegerField
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null = False, blank=False, editable = False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total and update the order total .
        """
        # Checks if the order number attribute of the current instance of the model is not set or empty if so 
        # it generates a order number
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.order.order_number