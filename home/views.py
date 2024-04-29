from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from celeb_profile.models import CelebRequest, CelebProfile
from products.models import Product


def index(request):
    """ A view to return the index page """

    celeb_profiles = CelebProfile.objects.filter(display_on_home=True)
    products = Product.objects.filter(display_on_home=True)

    template = 'home/index.html'
    context = {
        'celeb_profiles': celeb_profiles,
        'products': products,
    }

    return render(request, template, context)


def privacy(request):
    """A view to return the privacy page"""
    
    return render(request, 'home/privacy.html')