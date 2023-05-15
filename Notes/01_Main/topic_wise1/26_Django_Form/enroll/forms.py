from django import forms


# creating form class
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
