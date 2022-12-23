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
    # Default: template_name_suffix = '_list'
    # change to another template name suffix
    template_name_suffix = '_get'
    # add new template name here 'school/student_get.html' is also supported & 'school/student.html' is also supported
    template_name = 'school/students.html'
    # NOTE: custom template_name have higher priority to get render if both of the template is located

    # we can order the list of data with some field
    ordering = ['name']
    # Ordering with name

    # If you want to filter the data like if you want to add 'WHERE' clause on SQL Query then use this method:
    def get_queryset(self):
        # default:
        # return super().get_queryset()

        # With Filter
        return Student.objects.filter(course='Python')

    def get_context_data(self, *args, **kwargs):
        # this method return the context data into template
        context = super().get_context_data(*args, **kwargs)

        # we can add and return new context data from here as well
        context["fresher"] = Student.objects.all().order_by('name')
        return context

    # Setting dynamic template
    def get_template_names(self):
        # this method help you to set a dynamic template based on condition if you want
        if self.request.COOKIES['user'] == 'roman':
            template_name = 'school/roman.html'
        else:
            template_name = self.template_name

        # Default call:
        # return super().get_template_names()

        # return new template
        return [template_name]
