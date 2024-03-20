from django.shortcuts import render, redirect
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the contents in the users shopping bag """

    return render(request, 'bag/bag.html', {})



def add_to_bag(request, product_id):
    """ Add a quantity of the product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)




def delete_bag(request):
    pass

def update_bag(request):
    pass