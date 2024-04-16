from django.shortcuts import render, get_object_or_404
from .models import Product 
from celeb_profile.models import CelebRequest

def all_products(request):
    """ A view to show all products """

    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'query': query, 
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    # Product.objects.filter used to retrieve products from database
    # celeb_profile=product.celeb_profile filters products where the celeb_profile 
    celeb_profile_products = Product.objects.filter(
        celeb_profile=product.celeb_profile
    )

    context = {
        'product': product,
        'celeb_profile_products': celeb_profile_products,
    }

    return render(request, 'products/product_detail.html', context)