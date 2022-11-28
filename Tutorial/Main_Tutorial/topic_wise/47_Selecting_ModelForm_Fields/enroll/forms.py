from django import forms
from .models import User


class UserRegistration(forms.ModelForm):

    class Meta:
        model = User

        # passing specific field that we want to use to create a form
        # fields = ['name', 'email', 'password']

        # passing '__all__' value to render the all model field into form
        # fields = '__all__'

        # passing the specific field that you want to exclude from the model fields while creating the form
        # exclude = ['name']
        exclude = ('name',)
