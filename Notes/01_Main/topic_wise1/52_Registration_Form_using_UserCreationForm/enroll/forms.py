from django.contrib.auth.forms import UserCreationForm
# if you want to create form inherited from 'UserCreationForm' then we also need to get the model that it uses
from django.contrib.auth.models import User
from django import forms


# created form class inherited from 'UserCreationForm'
class SighUpForm(UserCreationForm):
    # because 'password1' & 'password2' are not the part of 'User' Model we have to edit those here
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # extending new fields into this form
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': "Email"}
