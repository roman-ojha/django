from django.shortcuts import render
from .forms import StudentRegistration


def showFormData(request):
    form = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
