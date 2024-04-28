from django import forms
from .models import contactMessage


class contactMessageForm(forms.ModelForm):
    class Meta:
        model = contactMessage
        fields = ('Name', 'email', 'subject', 'message')
