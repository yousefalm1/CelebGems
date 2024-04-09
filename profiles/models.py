from django.db import models
# this means that after a model instance is saved it is sent by django to the entire applications 
from django.db.models.signals import post_save
# To receive these signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class UserProfile(models.Model):
    """
    This is the user profile all users will have when the create an account 
    with allauth they will be able to fill in the info when they click the profile tab
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country ', null=False, blank=False)

    def __str__(self):
        return self.user.username

# Each time a user object is saved it will automatically either create a profile for them if the user has just been created 
# Or just save the profile if the user already existed 
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile 
    """
    # checks if new user instance was created 
    # if so it creates a corresponding userprofile instance for that user 
    if created:
        UserProfile.objects.create(user=instance)
    # Existing Users: just save the existing userprofile associated 
        instance.userprofile.save()     




