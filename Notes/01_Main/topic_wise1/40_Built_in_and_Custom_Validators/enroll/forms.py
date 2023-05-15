from django import forms

# first import validators
from django.core import validators

# creating custom validator function


def start_with_r(value):
    if value[0] != 'r':
        raise forms.ValidationError("Name should start with 'r' char")


class StudentRegistration(forms.Form):
    # now we have to pass the list of validators into formField
    name = forms.CharField(validators=[validators.MaxLengthValidator(
        10), validators.MinLengthValidator(5), start_with_r])
    email = forms.EmailField()
