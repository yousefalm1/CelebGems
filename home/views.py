from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from celeb_profile.models import CelebRequest, CelebProfile
from products.models import Product

def index(request):
    """ A view to return the index page """

    celeb_profiles = CelebProfile.objects.filter(display_on_home=True)
    products = Product.objects.filter(display_on_home=True)

    # default value if user is not authenticated  
    has_approved_request = False

    if request.user.is_authenticated:
    # Check if the current user has an approved request
        has_approved_request = CelebRequest.objects.filter(user=request.user, approved=True).exists()

    template = 'home/index.html'
    context = {
        'celeb_profiles': celeb_profiles,
        'has_approved_request': has_approved_request,
        'products': products,
    }

    return render(request, template, context)




