from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# we will import the form that we create using 'UserChangeForm'
from .forms import SighUpForm, EditUserProfileForm


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
        return HttpResponseRedirect('/enroll/profile')

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
                return HttpResponseRedirect('/enroll/profile/')
            else:
                form = AuthenticationForm()
                messages.error(request, "Login fail")
        else:
            messages.error(request, "Authentication failed")
    else:
        form = AuthenticationForm()
    return render(request, 'enroll/login.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # 'UserChangeForm' contain the form that will help to change the user info
            # But we don't want every field that this form provide in that case we will change the Form by create our new form and inherit from this Form
            # so we created the 'EditUserProfileForm' form that will contain the minimum form that is required for profile page

            # if method is POST and user send the data to change then we will pass the data to form we well
            form = EditUserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                # if given form data is valid the we will save the changed data
                form.save()
                messages.success(request, "You profile get updated")
        else:
            # for GET request we will just pass the user edit form
            form = EditUserProfileForm(instance=request.user)
        name = request.user
        return render(request, 'enroll/profile.html', {'name': name, 'form': form})
    else:
        messages.error(
            request, "You are not authenticated, Please login first")
        return HttpResponseRedirect('/enroll/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/login/')


def user_change_pass(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Access Denied, You are not authenticated")
        return HttpResponseRedirect('/enroll/login/')
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return HttpResponseRedirect('/enroll/profile/')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'enroll/change_password.html', {'form': form})
