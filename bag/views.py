from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product

def view_bag(request):
    """ A view that renders the contents in the users shopping bag """

    return render(request, 'bag/bag.html', {})

def add_to_bag(request, product_id):
    """ Add a quantity of the product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['products_by_size'].keys():
                bag[product_id]['products_by_size'][size] += quantity
            else:
                bag[product_id]['products_by_size'][size] = quantity
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

def adjust_bag(request, product_id):
    """ Adjust the quantity of the product """

    quantity = int(request.POST.get('quantity'))

    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[product_id]['product_by_size'][size] = quantity
        else:
            del bag[product_id]['product_by_size'][size]
            if not bag[product_id]['product_by_size']:    
                bag.pop(product_id)            
    else:
        if quantity > 0:
            bag[product_id] = quantity
        else:
            bag.pop[product_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, product_id):
    """ Remove the item from the shopping bag """

    try:
        size = None
        if 'size' in request.POST:
            size = request.POST['size']

        bag = request.session.get('bag', {})

        if str(product_id) in bag: 
            if size:
                del bag[str(product_id)]['products_by_size'][size]
                if not bag[str(product_id)]['products_by_size']:
                    bag.pop(str(product_id))
            else:
                bag.pop(str(product_id))
                
        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

