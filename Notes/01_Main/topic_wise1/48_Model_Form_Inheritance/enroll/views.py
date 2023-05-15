from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration
from .models import User


def student_registration(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': form})


def teacher_registration(request):
    if request.method == "POST":
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = TeacherRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
