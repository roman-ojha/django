from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import SighUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib.auth.models import User


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
    if request.user.is_authenticated:
        pass
    else:
        return HttpResponseRedirect('/enroll/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/login/')
