from django.shortcuts import render
# now here we will import the form that django auth provide us and we will use it for user registration
from django.contrib.auth.forms import UserCreationForm

# using inherited form from 'UserCreationForm'
from .forms import SighUpForm

from django.contrib import messages


def sign_up(request):
    # this process had already done in before tutorial
    if request.method == "POST":
        # 'UserCreationForm' contain the form that is required to create the new user
        form = UserCreationForm(request.POST)

        # But by default this form only consist of 'username', 'password', 'conform password'
        # but if we want to add extra field into it then we will create the new Form class that will inherited from 'UserCreationForm'
        form = SighUpForm(request.POST)

        if form.is_valid():
            # if user input is valid then we will save the user into database
            form.save()

            # after we created the user we will add the new message using django message framework
            messages.success(request, "Register User Successfully")
    else:
        # form = UserCreationForm()
        form = SighUpForm()
    return render(request, 'enroll/signup.html', {'form': form})
