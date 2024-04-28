from django.db import models
from django.db.models.signals import post_save
# To receive these signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    This is the user profile all users will have when the create an account
    with allauth they will be able to fill in the info when they
    click the profile nav link
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


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
