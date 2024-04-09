from .models import CelebRequest

def celeb_profile_status(request):
    if request.user.is_authenticated:
        has_approved_request = True  
    else:
        has_approved_request = False

    return {'has_approved_request': has_approved_request}