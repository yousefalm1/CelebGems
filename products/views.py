from django.shortcuts import render, get_object_or_404
from .models import Product 
from celeb_profile.models import CelebRequest

# Create your views here.


def all_products(request):
    """ A view to show all products """

    has_approved_request = CelebRequest.objects.filter(user=request.user, approved=True).exists()

    products = Product.objects.all()

    context = {
        'products': products,
        'has_approved_request': has_approved_request
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    has_approved_request = CelebRequest.objects.filter(user=request.user, approved=True).exists()


    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'has_approved_request': has_approved_request
    }

    return render(request, 'products/product_detail.html', context)