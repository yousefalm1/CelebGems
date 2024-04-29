from django.db import models
from celeb_profile.models import CelebProfile
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


class Product(models.Model):

    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    small_description = models.TextField(
        max_length=100, blank=False, default=''
    )
    product_specifications = models.TextField(blank=False)
    availability_shipping_info = models.TextField(blank=False)

    HAS_SIZES_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]
    has_sizes = models.BooleanField(
        default=False, choices=HAS_SIZES_CHOICES, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')
    product_id = models.AutoField(primary_key=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    # 'celeb_profile.CelebProfile' this is the app and where the model is
    celeb_profile = models.ForeignKey(
        'celeb_profile.CelebProfile', on_delete=models.CASCADE,
        related_name='products', blank=True, null=True
    )
    display_on_home = models.BooleanField(default=False)

    def clean(self):
        """
        Clean method to perform validation logic before
        saving the model instance.
        """
        if self.display_on_home:
            displayed_products_count = Product.objects.filter(
                display_on_home=True
            ).count()
            if displayed_products_count >= 3:
                raise ValidationError(
                    'Only three products can appear on the home page.'
                )

    def save(self, *args, **kwargs):
        """
        Save method to call the clean method and save
        the model instance to the database.
        """
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
