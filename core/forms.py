"""
Django forms for the portfolio platform.
"""
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form with validation and spam protection."""

    # Honeypot field for basic spam protection
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        label='',
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'company', 'job_role', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Name *',
                'required': True,
                'id': 'contact-name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Email *',
                'required': True,
                'id': 'contact-email',
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Company (Optional)',
                'id': 'contact-company',
            }),
            'job_role': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Job Role (Optional)',
                'id': 'contact-role',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Your Message *',
                'required': True,
                'rows': 5,
                'id': 'contact-message',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        # If honeypot field is filled, it's likely a bot
        if cleaned_data.get('website'):
            raise forms.ValidationError("Spam detected.")
        return cleaned_data

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        if len(message.strip()) < 10:
            raise forms.ValidationError("Please write a message of at least 10 characters.")
        return message
