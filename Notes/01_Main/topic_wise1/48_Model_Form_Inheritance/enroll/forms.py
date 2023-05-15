from django import forms
from .models import User


# creating the base class ModelForm
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name', 'email', 'password']


# create the child class ModelForm inherited from 'StudentRegistration'
class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = ['teacher_name', 'email', 'password']
