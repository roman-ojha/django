from django.shortcuts import render
from .forms import UserRegistration
from .models import User


def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = UserRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
