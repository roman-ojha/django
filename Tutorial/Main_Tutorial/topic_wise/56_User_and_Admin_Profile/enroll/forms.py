from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SighUpForm(UserCreationForm):
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': "Email"}


class EditUserProfileForm(UserChangeForm):
    # to not show change password we will set password to None
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'date_joined', 'last_login', 'is_active']
        labels = {"email": "Email"}
