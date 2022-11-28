from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SighUpForm
from django.contrib import messages

# importing required function for this tutorial
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    if request.method == "POST":
        form = SighUpForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Register User Successfully")
    else:
        form = SighUpForm()
    return render(request, 'enroll/signup.html', {'form': form})


def sign_in(request):
    # if user is already logged in then we will redirect to profile page
    if request.user.is_authenticated:
        return HttpResponseRedirect('/enroll/profile')

    if request.method == 'POST':
        # django 'AuthenticationForm' provide us the form to authenticate the user for login
        # AuthenticationForm(<request>, <data>)
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # after validate we will get the cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # now we will authenticate the user using 'username' & 'password'
            # if it get authenticate then we will get the user
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                # if user exist then we will login
                login(request, user)
                # after we login we will redirect to profile page
                messages.success(request, "Logged in successfully")
                return HttpResponseRedirect('/enroll/profile/')
            else:
                # if user doesn't exist on database then we will create an error message to show to login page
                form = AuthenticationForm()
                messages.error(request, "Login fail")
        else:
            messages.error(request, "Authentication failed")
    else:
        form = AuthenticationForm()
    return render(request, 'enroll/login.html', {'form': form})


# for user profile page
def profile(request):
    # 'profile' page can only be able to access by the user
    # so we will check is the requested user is authenticated or no
    if request.user.is_authenticated:
        # now here we can access the user data
        name = request.user
        return render(request, 'enroll/profile.html', {'name': name})
    else:
        messages.error(
            request, "You are not authenticated, Please login first")
        return HttpResponseRedirect('/enroll/login')


def user_logout(request):
    # logging out user
    logout(request)
    return HttpResponseRedirect('/enroll/login/')
