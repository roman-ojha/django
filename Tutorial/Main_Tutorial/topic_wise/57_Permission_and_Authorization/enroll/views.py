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
            # we will check is the requested user is admin or normal user
            # for that we will check is the requested user is superuser or not
            if request.user.is_superuser:
                # if user is superuser then we will create Admin form for POST request to validated
                form = EditAdminProfileForm(
                    request.POST, instance=request.user)
                # so if user is Admin then we will also get the data of all the user and send it into the template
                users = User.objects.all()
            else:
                form = EditUserProfileForm(request.POST, instance=request.user)
                users = None
            if form.is_valid():
                form.save()
                messages.success(request, "You profile get updated")
        else:
            # we will check is the requested user is admin or normal user
            # for that we will check is the requested user is superuser or not
            if request.user.is_superuser:
                # if user is superuser then we will create Admin form rather then normal user form
                form = EditAdminProfileForm(instance=request.user)

                # so if user is Admin then we will also get the data of all the user and send it into the template
                users = User.objects.all()
            else:
                form = EditUserProfileForm(instance=request.user)
                users = None
        name = request.user
        return render(request, 'enroll/profile.html', {'name': name, 'form': form, 'users': users})
    else:
        messages.error(
            request, "You are not authenticated, Please login first")
        return HttpResponseRedirect('/enroll/login/')


# Function to render specific user detail only Admin user can access this
def user_detail(request, id):
    if request.user.is_authenticated:
        # only super user can get the user detail
        if request.user.is_superuser:
            # now we will get the user data
            user = User.objects.get(pk=id)
            # and also we will render the form
            # and we know Admin form have access to every field so we will render the Admin form rather
            form = EditAdminProfileForm(instance=user)
            return render(request, 'enroll/userdetail.html', {'form': form, 'user': user})
        else:
            messages.warning(request, "Access Denied")
            return HttpResponseRedirect('/enroll/profile/')
    else:
        messages.warning(request, "You are not authenticated")
        return HttpResponseRedirect('/enroll/login/')


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
