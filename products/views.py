from django.shortcuts import render, get_object_or_404
from .models import Product 
from celeb_profile.models import CelebRequest

# Create your views here.


def all_products(request):
    """ A view to show all products """


    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """


    # For nav
    has_approved_request = CelebRequest.objects.filter(user=request.user, approved=True).exists()
    # For nav

    product = get_object_or_404(Product, pk=product_id)


    # Product.objects.filter used to retrieve products from database
    # celeb_profile=product.celeb_profile filters products where the celeb_profile 
    celeb_profile_products = Product.objects.filter(celeb_profile=product.celeb_profile)

    context = {
        'product': product,
        'has_approved_request': has_approved_request,
        'celeb_profile_products': celeb_profile_products,
    }

    return render(request, 'products/product_detail.html', context)