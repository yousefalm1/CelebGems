from .models import CelebRequest

def celeb_profile_status(request):
    has_approved_request = False
    
    if request.user.is_authenticated:
        # Check if the user has an approved request for a celebrity profile
        has_approved_request = CelebRequest.objects.filter(user=request.user, approved=True).exists()
        
    return {'has_approved_request': has_approved_request}