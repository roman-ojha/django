from django import forms
from .models import User
from django.core import validators


class UserRegistration(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name': "Enter Name", 'email': "Enter Email",
                  'password': "Enter Password"}
        help_text = {'name': "Your Name"}
        error_messages = {'email': {'required': "Email is required"}, 'password': {
            'required': 'Password is required'}}
        widgets = {'password': forms.PasswordInput(), 'name': forms.TextInput(
            attrs={'class': 'text-input', 'placeholder': "Enter You Name"})}

    def clean_name(self):
        return self.cleaned_data['name']
