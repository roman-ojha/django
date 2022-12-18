from django.shortcuts import render
from .models import Student, ProxyStudent


def home(request):
    # accessing all the student with different manager name 'students'
    students = Student.students.all()

    # using the custom manager to query the data
    students = Student.students_custom.all()

    # using custom manager custom method to query the data
    students = Student.students_custom.get_stu_roll_range(30, 50)

    # querying using 'ProxyStudent' model
    students = ProxyStudent.students_custom.get_stu_roll_range(30, 50)
    return render(request, 'school/home.html', {'students': students})
