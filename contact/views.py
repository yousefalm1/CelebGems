from django.shortcuts import render, redirect
from .forms import contactMessageForm

def contact_page(request):
    """
    
    """
    if request.method == 'POST':
        form = contactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us_success')

    else:
        form = contactMessageForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def contact_us_success(request):
    return render(request, 'contact/contact_us_success.html')