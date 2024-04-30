
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import CelebRequest, CelebProfile
from products.models import Product
from .forms import (
    CelebRequestForm,
    CelebProfileForm,
    CelebAddProductForm,
    EditProductForm
)


def all_celebrities(request):
    """A View to show all celebrities."""
    celeb_profile = CelebProfile.objects.all()

    template = 'celeb_profile/celebrities.html'

    context = {
        'celeb_profile': celeb_profile,
    }

    return render(request, template, context)


def celeb_profile(request, user_id):
    """A view so all customers are able to see the celeb profile."""
    # Retrieve the CelebProfile object with the given username
    celeb_profile = get_object_or_404(CelebProfile, user_id=user_id)

    products_added = celeb_profile.products_added.all()

    # Pass the celeb_profile object to the template
    return render(
        request, 'celeb_profile/celeb_profile_consumer.html',
        {'celeb_profile': celeb_profile, 'products_added': products_added}
    )


def delete_product(request, product_id):
    """ A view to delete the product in the celeb profile page """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('delete_product_success')


def delete_product_success(request):
    """A view to display a success page once the user."""


def edit_product(request, product_id):
    """A view to edit a product that a user clicked to edit"""

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('edit_product_success',
                        kwargs={'product_id': product_id})
            )

    form = EditProductForm(instance=product)

    return render(
        request, 'celeb_profile/edit_product.html',
        {'form': form, 'product': product}
    )


def edit_product_success(request, product_id):
    """A view to to show the success of editing a product."""

    product = get_object_or_404(Product, pk=product_id)
    return render(
        request, 'celeb_profile/edit_product_success.html',
        {'product': product}
    )


def add_product(request):
    """A view to add a new product to a celebrity's profile."""
    if request.method == 'POST':
        form = CelebAddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            celeb_profile = request.user.celeb_profile
            celeb_profile.products_added.add(product)
            return redirect('add_product_success')
    else:
        form = CelebAddProductForm()
    return render(request, 'celeb_profile/add_product.html', {'form': form})


def add_product_success(request):
    """A view to show a success page once the user has added there product."""

    return render(request, 'celeb_profile/add_product_success.html')


def edit_celeb_profile(request):
    """.A view to edit the celeb profile and be given a confirmation."""

    # Gets the celeb profile for the current user logged in
    celeb_profile = get_object_or_404(CelebProfile, user=request.user)

    # If the form is submitted (POST request )
    if request.method == 'POST':
        # Create a form with the pre data of the celeb profile
        form = CelebProfileForm(
            request.POST, request.FILES, instance=celeb_profile
        )
        # Checks if the form is valid
        if form.is_valid():
            # Save the form to celeb profile which updates it
            form.save()
            # user goes back to the celeb profile page
            return redirect('edit_celeb_profile_confirmation')
    else:
        form = CelebProfileForm(instance=celeb_profile)

    context = {
        'form': form,
    }

    return render(request, 'celeb_profile/edit_celeb_profile.html', context)


def edit_celeb_profile_confirmation(request):
    """ A view to display the confirmation page."""

    return render(
        request, 'celeb_profile/edit_celeb_profile_confirmation.html'
    )


def celeb_profile_page(request,):
    """ A view to display the user's CelebProfile."""

    # Check if a CelebProfile already exists for the current user
    existing_celeb_profile = CelebProfile.objects.filter(
        user=request.user
    ).exists()

    if existing_celeb_profile:
        # If a CelebProfile exists, retrieve it
        celeb_profile = get_object_or_404(CelebProfile, user=request.user)

        products_added = celeb_profile.products_added.all()

        context = {
            'celeb_profile': celeb_profile,
            'products_added': products_added,
        }

        # Render the CelebProfile using the 'celeb_profile.html' template
        return render(request, 'celeb_profile/celeb_profile.html', context)
    else:
        # If no CelebProfile exists, redirect the user to create one
        return redirect('create_celeb_profile_page')


def create_celeb_profile_page(request):
    """A view to display and handle creating the celeb profile."""

    if request.method == 'POST':
        form = CelebProfileForm(request.POST, request.FILES)
        if form.is_valid():
            celeb_profile = form.save(commit=False)
            celeb_profile.user = request.user
            celeb_profile.save()
            return redirect('celeb_profile_page')
    else:
        form = CelebProfileForm()

    return render(
        request, 'celeb_profile/create_celeb_profile.html', {'form': form}
    )


def request_celeb_profile_page(request):
    """A view display the and handle the celeb profile request form."""

    existing_request = CelebRequest.objects.filter(user=request.user).exists()

    if existing_request:
        return redirect('request_already_submitted')

    if request.method == 'POST':
        form = CelebRequestForm(request.POST)
        if form.is_valid():
            celeb_request = form.save(commit=False)
            celeb_request.user = request.user
            celeb_request.save()
            return redirect('request_celeb_profile_submitted')
    else:
        form = CelebRequestForm()

    return render(
        request, 'celeb_profile/request_celeb_profile.html', {'form': form}
    )


def request_celeb_profile_submitted(request):
    """A view to render the confirmation page after
    submitting the CelebRequestForm.
    """

    submitted_user = request.user  # Get the user who submitted the request

    submitted_user = request.user
    context = {
        'submitted_user': submitted_user,
    }
    return render(
        request, 'celeb_profile/request_celeb_profile_form_submitted.html',
        context
    )


def request_already_submitted(request):
    """A view to render the request already submitted."""

    return render(request, 'celeb_profile/request_already_submitted.html')
