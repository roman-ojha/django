from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from .models import Student

# We will create a view for Creating Object as well as Update Object


# View to create new 'Student' object
class CreateStudentView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

# View to update 'Student' object


class UpdateStudentView(UpdateView):
    # here we will specify on which model you want to update data
    model = Student
    # in which field you want to update data
    fields = ['name']
