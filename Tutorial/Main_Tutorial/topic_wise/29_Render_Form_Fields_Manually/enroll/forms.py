from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(help_text="Enter Name")
    email = forms.EmailField(initial='roman@gmail.com',
                             help_text='Enter Email')
