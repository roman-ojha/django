from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms

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
    fields = ['name', 'email', 'password']

    success_url = '/thanks/'

    # But we have to pass the dynamic url value 'pk' to update the specific data

    # By default this view uses the same template name as the 'Createview' one

    # Adding class inside form field
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(
            attrs={'class': 'name-field'})
        form.fields['password'].widget = forms.PasswordInput(
            render_value=True, attrs={'class': 'password-field'})
        # we have to pass 'render_value' as True if you want to populate the password value into Password form field
        return form

    # And the another way to add class inside for is to use 'ModelForm' that say we that we did inside 'CreateView' Tutorial
    # NOTE: for that we have to provide 'model' property as well
    # form_class = <form_class>
    # model = <need_to_provide_model>
    # template_name = <need_to_provide_template_name>
