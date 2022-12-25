from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms


class CreateStudentView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'


class UpdateStudentView(UpdateView):
    model = Student
    fields = ['name', 'email', 'password']

    success_url = '/thanks/'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(
            attrs={'class': 'name-field'})
        form.fields['password'].widget = forms.PasswordInput(
            render_value=True, attrs={'class': 'password-field'})
        return form


# Delete View to delete model object
class DeleteStudentView(DeleteView):
    # providing model from where we want to delete
    model = Student

    # Success url after object get deleted
    success_url = '/create/'

    # Before deleting the object it will first redirect to the confirmation page
    # By default the template for confirmation page is '<model>_confirm_delete.html'
