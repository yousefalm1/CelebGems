from django.shortcuts import render, get_object_or_404, redirect

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """

    # query userprofile to find where user field matches the currently logged in user 
    # if userprofile is not found render 404 page
    profile = get_object_or_404(UserProfile, user=request.user)
    # since in the order model orders is the related name for user_profile 
    orders = profile.orders.all()

    # Instance puts the userprofile pre existing details in the form for when editing 
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)



def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
            

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
