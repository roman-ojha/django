from django.shortcuts import render

# importing forms class
from .forms import StudentRegistration


def showFormData(request):
    # creating object of form data to pass into template as object
    form = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form': form})
