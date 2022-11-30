from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import SighUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib.auth.models import User, Group


def sign_up(request):
    if request.method == "POST":
        form = SighUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            # while registering the user we will also add that user to some group
            group = Group.objects.get(name="Editor")
            # first we are getting the 'editor' group
            # now we will add the user to the group
            user.groups.add(group)

            messages.success(request, "Register User Successfully")
    else:
        form = SighUpForm()
    return render(request, 'enroll/signup.html', {'form': form})


def sign_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/enroll/dashboard/')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return HttpResponseRedirect('/enroll/dashboard/')
            else:
                form = AuthenticationForm()
                messages.error(request, "Login fail")
        else:
            messages.error(request, "Authentication failed")
    else:
        form = AuthenticationForm()
    return render(request, 'enroll/login.html', {'form': form})


def dashboard(request):
    # NOTE: we will add and remove permission to the user from '/admin' panel
    # and we will check that permission inside view template as per that we will show the required data
    # also we will create group and add user to that group and we know how permission work with group as well
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html', {'username': request.user.username})
    else:
        return HttpResponseRedirect('/enroll/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/login/')
