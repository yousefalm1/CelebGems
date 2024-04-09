from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
# from checkout import Order
from .forms import UserProfileForm

def profile(request):
    """
    View function for displaying the user's profile.

    Retrieves the user's profile based on the currently logged-in user.
    If the profile is not found, a 404 page is rendered.

    Retrieves all orders associated with the user's profile.
    """
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
    """
    View function for editing user profile.

    If the request method is POST, the function processes the form data submitted
    by the user to update their profile information. If the form data is valid,
    the profile is updated, and the user is redirected to their profile page.

    If the request method is GET, the function renders the edit profile form with
    the user's current profile information pre-filled.
    """
    
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