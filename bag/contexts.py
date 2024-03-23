from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    # Creates an empty list to store info about the products in the shopping bag
    bag_products = []
    # Creates a variable to keep track of the total cost of all the products in the shopping bag
    total = 0
    # Creates a variable to count the total number of products in the bag
    product_count = 0
    # Get the shopping bag from the session if no bag it creates a dict 
    bag = request.session.get('bag', {})  

    # loops thru each bag item in bag using bag.items
    for product_id, product_data in bag.items():
        # Checks if product_data is an integer (which means the product has no size variations)
        if isinstance(product_data, int):
            # Gets the corresponding product from the database 
            product = get_object_or_404(Product, pk=product_id)
            # Calculates the total cost of all products in bag and updates the product count 
            total += product_data * product.price
            product_count += product_data
            # appends the info to the bag_products list
            bag_products.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product,
            })
        else:
            # if products data is not a integer meaning it has sizes 
            product = get_object_or_404(Product, pk=product_id)
            # it loops thru each size and quantity in the product data 'products_by_size
            for size, quantity in product_data['products_by_size'].items():
                # calculates the total cost and updates the product count 
                total += quantity * product.price
                product_count += quantity
                # appends the info about product and size to bag_products list 
                bag_products.append({
                    'product_id': product_id,
                    'quantity': product_data,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    # The whole project can use this since its added to settings
    context = {
        'bag_products': bag_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
