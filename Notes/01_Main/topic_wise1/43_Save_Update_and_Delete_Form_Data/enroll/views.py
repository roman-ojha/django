from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


def register(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # creating a new user object
            reg = User(name=name, email=email, password=password)

            # if we will pass the id while creating the user then it will update the data
            reg = User(id=3, name=name, email=email, password=password)
            # saving the user
            reg.save()

            # Delete Data
            reg = User(id=3)
            reg.delete()
    else:
        form = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
