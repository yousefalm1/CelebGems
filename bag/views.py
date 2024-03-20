from django.shortcuts import render
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the contents in the users shopping bag """

    return render(request, 'bag/bag.html')