from django.db import models
from celeb_profile.models import CelebProfile  
from django.core.exceptions import ValidationError




class Product(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    product_specifications = models.TextField()
    availability_shipping_info = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True) 
    image = models.ImageField(null=True, blank=True)
    product_id = models.AutoField(primary_key=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    # 'celeb_profile.CelebProfile' this is the app and where the model is 
    celeb_profile = models.ForeignKey('celeb_profile.CelebProfile', on_delete=models.CASCADE, related_name='products', blank=True, null=True)


    display_on_home = models.BooleanField(default=False)

# clean() method where you can put validation logic to ensure that the data being saved is valid.
    def clean(self):
        # Checks if the attribute display_on_true on the current instance of the model is set to true 
        if self.display_on_home and Product.objects.filter(display_on_home=True).count >= 3:
            raise ValidationError('Only three products can appear on the home page.')

    
    def __str__(self):
        return self.name

