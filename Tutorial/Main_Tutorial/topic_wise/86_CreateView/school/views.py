from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms
from .forms import StudentForm


# Create your views here.
class CreateStudentView(CreateView):
    # passing the mode where we want to save the valid form that we get from user
    model = Student
    # now the field that we provide these are the field from which it will create a new form and send it into the template to get render
    fields = ['name', 'email', 'password']

    # success url after user submit data and form get validate and it get save into database
    # success_url = '/thanks/'
    # we can use another way to redirect after success is through 'get_absolute_url' function that we define inside 'Student' model

    # Default template_name = 'school/student_form.html'
    # Custom template_name
    # template_name = 'school/form.html'

    # Now we will add a custom class inside form elements so that we can add css style inside form
    # for that we will override get_form method
    def get_form(self):
        form = super().get_form()
        # adding classname inside form tags
        # we can add all the attributes inside this function
        form.fields['name'].widget = forms.TextInput(
            attrs={'class': 'name-field'})
        form.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'password-field'})

        return form

    # Different way to add classname inside forms tag are using Model form
    # Now we cant provide 'model' property inside this class we have to use 'form_class' rather
    # and we created this form inside './forms.py'
    # form_class = StudentForm


class ThankTemplateView(TemplateView):
    template_name = 'school/thanks.html'


# we will show the save 'Student' data through this view
class StudentDetailView(DetailView):
    model = Student
