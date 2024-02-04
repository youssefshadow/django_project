# contact/forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Votre nom',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Votre adresse e-mail',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Votre message',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
