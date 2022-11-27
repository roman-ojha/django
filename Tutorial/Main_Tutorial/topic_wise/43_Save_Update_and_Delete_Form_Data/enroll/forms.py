from django import forms

from django.core import validators


class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter your name'})
    email = forms.EmailField(
        error_messages={'required': 'Enter your Email'}, min_length=5, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={
                               'required': 'Enter your Password'}, min_length=5, max_length=50)

    # here we are giving the class name of the error if it occur
    error_css_class = 'error'
    required_css_class = 'required'
