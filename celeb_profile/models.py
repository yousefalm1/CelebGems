from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


class CelebRequest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, unique=True
    )
    occupation = models.CharField(max_length=100)
    reasons = models.TextField()
    social_media = models.URLField(max_length=200, blank=True, null=True)
    target_audience = models.CharField(max_length=200, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Request from {self.user.username}"


class CelebProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=1,
        related_name='celeb_profile',
    )
    social_media = models.URLField(max_length=200, blank=True, null=True)
    profile_name = models.CharField(max_length=100)
    bio = models.TextField()
    small_bio = models.CharField(max_length=100, default='')
    image = CloudinaryField('image', default='placeholder')
    products_added = models.ManyToManyField('products.Product', blank=True)
    # Displays celeb profile on homepage when clicked
    display_on_home = models.BooleanField(default=False)

    # Used  for this
    def clean(self):
        """
        Check if more than three CelebProfiles
        have appear_on_home set to True
        """

        if self.display_on_home and CelebProfile.objects.filter(
            display_on_home=True
        ).count() >= 3:
            raise ValidationError(
                'Only three CelebProfiles can appear on the home page.'
            )

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the model instance before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
