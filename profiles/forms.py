from django import forms
from .models import UserProfile

class UserProfileFrom(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        