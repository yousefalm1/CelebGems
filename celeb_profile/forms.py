from django import forms
from .models import CelebRequest, CelebProfile

class CelebRequestForm(forms.ModelForm):
    class Meta:
        model = CelebRequest
        fields = ['occupation', 'reasons', 'social_media', 'target_audience', 'additional_information']
