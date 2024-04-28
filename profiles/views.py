from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from checkout.models import Order
# from checkout import Order
from .forms import UserProfileForm


def profile(request):
    """
    View function for displaying the user's profile.

    Retrieves the user's profile based on the currently logged-in user.
    If the profile is not found, a 404 page is rendered.

    Retrieves all orders associated with the user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()
    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def edit_profile(request):
    """View function for editing user profile."""

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


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)