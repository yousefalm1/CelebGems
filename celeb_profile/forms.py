from django import forms
from .models import CelebRequest, CelebProfile 
from products.models import Product


class CelebRequestForm(forms.ModelForm):
    class Meta:
        model = CelebRequest
        fields = ['occupation', 'reasons', 'social_media', 'target_audience', 'additional_information']


class CelebProfileForm(forms.ModelForm):
    class Meta:
        model = CelebProfile
        fields = ['profile_name', 'bio', 'image', 'image_url'] 



class CelebAddProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','product_specifications','availability_shipping_info', 'price', 'quantity_in_stock', 'image_url', 'image']


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','product_specifications','availability_shipping_info', 'price', 'quantity_in_stock', 'image_url', 'image']
