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
    size = None
    if 'product_size' in request.POST:
        size = request.POST['size']
    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['products_by_size'].keys():
                bag[product_id]['products_by_size'][size] += quantity
            else:
                bag[product_id]['products_by size'][size] = quantity
        else:
            bag[product_id] = {'products_by_size': {size: quantity }}

    else:
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