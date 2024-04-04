from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileFrom


def profile(request):
    """ Display the user's profile. """

    # query userprofile to find where user field matches the currently logged in user 
    # if userprofile is not found render 404 page
    profile = get_object_or_404(UserProfile, user=request.user)
    # since in the order model orders is the related name for user_profile 
    orders = profile.orders.all()

    # Instance puts the userprofile pre existing details in the form for when editing 
    form = UserProfileFrom(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)