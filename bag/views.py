from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view that renders the contents in the users shopping bag """

    return render(request, 'bag/bag.html')