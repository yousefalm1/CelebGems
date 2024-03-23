from django.shortcuts import render, redirect
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the contents in the users shopping bag """

    return render(request, 'bag/bag.html', {})



def add_to_bag(request, product_id):
    """ Add a quantity of the product to the shopping bag """


    # Gets the quantity of the product the redirect_ulr and sets the size to None if there is a product size it get the product size
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # this retrieves the current bag of the session if no bag it it sets up an empty dict
    bag = request.session.get('bag', {})

    # Checks if size is selected for product
    if size:
        # then checks if product is already in bag
        if product_id in list(bag.keys()):
            # checks if the selected size for the product is already present in bag if so it adds to the quantity
            #  returns a view object containing all the keys (sizes) present in the products_by_size dictionary for the specific product identified by product_id.
            if size in bag[product_id]['products_by_size'].keys():
                bag[product_id]['products_by_size'][size] += quantity
            else:
                # if that size is not there but the product is there it creates a new line entry in the 'products_by_size' dict 
                bag[product_id]['products_by_size'][size] = quantity
        else:
            # if no  product in bag but has size
            bag[product_id] = {'products_by_size': {size: quantity }}

    # If the product has no size this code block is executed 
    else:
        # bag.keys() gets all the productIds(keys) from the bag dict
        # list(bag.keys()) converts these keys into a list
        # product_id in list(bag.keys()) checks if the product_id is present in this list of keys.
        if product_id in list(bag.keys()):
            # if product is in the bag it updated the quantity 
            bag[product_id] += quantity
        else:
            # or else it will add the the product along with the quantity to the bag
            bag[product_id] = quantity

    # Updates the bag data with the modified bag dict
    request.session['bag'] = bag
    print(request.session['bag'])
    # Redirects the user to a url after adding the product
    return redirect(redirect_url)




def delete_bag(request):
    pass

def update_bag(request):
    pass