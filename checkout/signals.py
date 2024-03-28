# this means that after a model instance is saved and deleted it is sent by django to the entire applications 
from django.db.models.signals import post_save, post_delete
# To receive these signals
from django.dispatch import receiver

from .models import OrderLineItem

# To Execute this function whenever the post save signal is sent 
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """

    # Access the order this specific item is related to and call the update_total method
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ 
    Update order total on lineitem delete
    """

    # Access the order this specific item is related to and call the update_total method
    instance.order.update_total()