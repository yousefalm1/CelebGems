from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product

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

def adjust_bag(request, product_id):
    """ Adjust the quantity of the product """

    # Gets the quantity of the product from the post request sent by the user then converts it to an integer
    quantity = int(request.POST.get('quantity'))

    size = None

    # check if product_size is in the post request (If it does then user has selected a size )
    if 'product_size' in request.POST:
        # if the size is there it gets the size from the POST request 
        # it accesses the value associated with the 'product_size' key in the request.POST dictionary 
        size = request.POST['product_size']
    # gets the shopping bag using the 'bag' key in the session dict if not there it returns an empty dict 
    bag = request.session.get('bag', {})

    # Checks if the size variable has a value
    if size:
        # is size is provided and has a quantity of greater than 0 
        if quantity > 0:
            # it sets the quantity of the product with the given size in th bag dict 
            # It accesses 'bag' dict by using the product_id as the key then accesses the nested dict 'product_by_size' to store the quantity for the specified size.
            bag[product_id]['product_by_size'][size] = quantity
        else:
            # If the quantity is 0 less it removes the product
            del bag[product_id]['product_by_size'][size]
            if not bag[product_id]['product_by_size']:    
                bag.pop(product_id)            
    #  if the product has no size 
    else:
        # If the product is greater then 0 it sets the quantity directly in the bag dict using the product_id as the key 
        if quantity > 0:
            bag[product_id] = quantity
        else:
            # if the product is 0 or less it removes it from the bag using the pop method on the bag dict with the product_id as the key 
            bag.pop[product_id]

    # After adjusting the contents of the bag dict it updates the session variable 'bag' with the modified 'bag' dict
    request.session['bag'] = bag
    # The code redirects the user to bag to the bag which will be updated 
    return redirect(reverse('view_bag'))

def remove_from_bag(request, product_id):
    """ Remove the item from the shopping bag """

    try:
        size = None
        if 'size' in request.POST:
            size = request.POST['size']

        bag = request.session.get('bag', {})

        # Check if product_id exists in the bag dictionary
        if str(product_id) in bag:  # Convert product_id to string for comparison
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

