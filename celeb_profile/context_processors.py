from .models import CelebRequest


def celeb_profile_status(request):
    has_approved_request = False
    if request.user.is_authenticated:
        has_approved_request = CelebRequest.objects.filter(user=request.user, approved=True).exists()
    return {'has_approved_request': has_approved_request}
