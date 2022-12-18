from django.shortcuts import render
from .models import Student


def home(request):
    # accessing all the student with different manager name 'students'
    students = Student.students.all()

    # using the custom manager to query the data
    students = Student.students_custom.all()
    return render(request, 'school/home.html', {'students': students})
