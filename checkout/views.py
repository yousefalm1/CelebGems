from django.shortcuts import redirect, reverse, render
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    """
    A view to handle the checkout process.

    Retrieves the shopping bag from the session. If the bag is empty, displays an error message and redirects the user to the products page.
    
    Initializes an instance of the order form for the checkout process.
    """
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse,('products') )
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = { 
        'order_form' : order_form
    }

    return render(request, template, context)