from django import forms
from .models import User
from django.core import validators


# Creating form using Model
class UserRegistration(forms.ModelForm):

    class Meta:
        # model that you want to use for creating form
        model = User

        # in order that we define the fields will get render on template
        fields = ['name', 'email', 'password']

        # define labels for field
        labels = {'name': "Enter Name", 'email': "Enter Email",
                  'password': "Enter Password"}

        # defining help_text
        help_text = {'name': "Your Name"}

        # error message on all field
        error_messages = {'email': {'required': "Email is required"}, 'password': {
            'required': 'Password is required'}}

        # defining widget
        widgets = {'password': forms.PasswordInput(), 'name': forms.TextInput(
            attrs={'class': 'text-input', 'placeholder': "Enter You Name"})}

    def clean_name(self):
        # here we can do validation as stuff if you want same as Form API
        return self.cleaned_data['name']
