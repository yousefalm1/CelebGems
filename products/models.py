from django.db import models
from celeb_profile.models import CelebProfile  # Import CelebProfile from the correct app



class Product(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True) 
    image = models.ImageField(null=True, blank=True)
    product_id = models.AutoField(primary_key=True)
    # 'celeb_profile.CelebProfile' this is the app and where the model is 
    celeb_profile = models.ForeignKey('celeb_profile.CelebProfile', on_delete=models.CASCADE, related_name='products', blank=True, null=True)


    def __str__(self):
        return self.name

