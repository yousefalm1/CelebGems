from django.shortcuts import render
from .forms import contactMessageForm

def contact_page(request):
    if request.method == 'POST':
        form = contactMessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = contactMessageForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)