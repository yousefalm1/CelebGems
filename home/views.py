from django.shortcuts import render
from celeb_profile.models import CelebRequest

def index(request):
    """ A view to return the index page """

    # Check if the current user has an approved request
    has_approved_request = CelebRequest.objects.filter(user=request.user, approved=True).exists()

    return render(request, 'home/index.html', {'has_approved_request': has_approved_request})
