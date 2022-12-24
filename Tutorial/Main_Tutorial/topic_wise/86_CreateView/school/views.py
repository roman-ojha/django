from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student


# Create your views here.
class CreateStudentView(CreateView):
    # passing the mode where we want to save the valid form that we get from user
    model = Student
    # now the field that we provide these are the field from which it will create a new form and send it into the template to get render
    fields = ['name', 'email', 'password']
