from django.shortcuts import render, HttpResponseRedirect
from .forms import SighUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# django provide use the form to change the password so we will import it
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm


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
        name = request.user
        return render(request, 'enroll/profile.html', {'name': name})
    else:
        messages.error(
            request, "You are not authenticated, Please login first")
        return HttpResponseRedirect('/enroll/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/login/')


# view to change the user password which contain Old password
def user_change_pass(request):
    # this view route can only be access by the authenticated user, those user that is already logged in
    if not request.user.is_authenticated:
        messages.warning(request, "Access Denied, You are not authenticated")
        return HttpResponseRedirect('/enroll/login/')
    if request.method == "POST":
        # 'PasswordChangeForm' will provide the form to change the password which will take 'user' as an argument
        # if it is POST method then we will also provide the data that we get
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            # after field get validated to save the password change we can save the form
            form.save()
            # after user change the password user session will not get authenticated so user can't login
            # so to update the session after user changed the password we will do this:
            update_session_auth_hash(request, form.user)

            messages.success(request, "Password Changed Successfully")

            return HttpResponseRedirect('/enroll/profile/')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'enroll/change_password.html', {'form': form})


# View to change the user password which out required Old password
def change_pass_with_out_old(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Access Denied, You are not authenticated")
        return HttpResponseRedirect('/enroll/login/')
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return HttpResponseRedirect('/enroll/profile/')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'enroll/change_password.html', {'form': form})
