from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student


# Creating generic class view
class StudentListView(ListView):
    model = Student
    # passing model while will run:
    # Student.object.all()

    # and we will get context data inside 'object_list' || 'student_list'
    # we can change the default context name for 'student_list'
    # but 'object_list' will get pass after changing context object name
    context_object_name = 'students'

    # default template name this view will render is 'school/student_list.html'
