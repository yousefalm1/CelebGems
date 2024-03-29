from django.shortcuts import redirect, reverse, render
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse,('products') )
    
    # Create an instance of the order form 
    order_form = OrderForm()
    # Create the template
    template = 'checkout.checkout.html'
    context = { 
        'order_form' : order_form
    }

    return render(request,template, context)