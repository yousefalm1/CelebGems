from django.shortcuts import render, redirect
from .forms import CelebRequestForm

# Create your views here.

def request_celeb_profile_page(request):
    """ A view display the and handle the celeb profile request form """

    if request.method == 'POST':
        form = CelebRequestForm(request.POST)
        if form.is_valid():
            celeb_request = form.save(commit=False) # creates a CelebRequest instance in memory without saving it to the database immediately. 
            celeb_request.user = request.user # assigns the current user to the user field of the CelebRequest instance.
            celeb_request.save() #  saves the modified CelebRequest instance to the database.
            return redirect('request_celeb_profile_submitted')
    else:
        form = CelebRequestForm()
    
    return render(request, 'celeb_profile/request_celeb_profile.html', {'form': form})



def request_celeb_profile_submitted(request ):
    """A view to render the confirmation page after submitting the CelebRequestForm."""

    submitted_user = request.user  # Get the user who submitted the request

    context = {
        'submitted_user' : submitted_user,
    }
    return render(request, 'celeb_profile/request_celeb_profile_form_submitted.html', context)