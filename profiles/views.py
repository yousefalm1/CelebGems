from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def profile(request):
    """
    Display user profile 
    """

    profile = UserProfile.objects.get(user=request.user) 

    context = {
        'profile': profile 
    }

    return render(request, 'templates/profiles/profile.html', context)