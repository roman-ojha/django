from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    # creating hidden field
    key = forms.CharField(widget=forms.HiddenInput())
