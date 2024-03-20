from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the contents in the users shopping bag """

    return render(request, 'bag/bag.html', {})



def add_bag(request):
    pass




def delete_bag(request):
    pass

def update_bag(request):
    pass