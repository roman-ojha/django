from django import forms


# creating form class
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    # this will generate label:
    # <label for="first_name">First name </label>
