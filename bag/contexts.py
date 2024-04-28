from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Retrieves the contents of the shopping bag from the session and calculates
    the total cost, quantity, and delivery charges.

    Iterates through each item in the shopping bag, including individual
    products and their sizes if applicable.
    Calculates the total cost of all items, taking into account any applicable
    delivery charges based on the total cost.

    Returns a dictionary containing information about the bag contents,
    including product details, total cost, delivery charges, and grand total.
    """

    bag_products = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, product_data in bag.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += product_data * product.price
            product_count += product_data
            bag_products.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, quantity in product_data['products_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_products.append({
                    'product_id': product_id,
                    'quantity': quantity,
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
