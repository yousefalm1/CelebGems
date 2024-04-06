from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from celeb_profile.models import CelebRequest, CelebProfile

def index(request):
    """ A view to return the index page """

    
    celeb_profile =  CelebProfile.objects.all()

    # default value if user is not authenticated  
    has_approved_request = False

    if request.user.is_authenticated:
    # Check if the current user has an approved request
        has_approved_request = CelebRequest.objects.filter(user=request.user, approved=True).exists()

    return render(request, 'home/index.html', {'has_approved_request': has_approved_request})
