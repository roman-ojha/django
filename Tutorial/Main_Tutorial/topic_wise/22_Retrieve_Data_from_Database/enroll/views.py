from django.shortcuts import render

# first we will import model class to access database table
from enroll.models import Student


def studentsInfo(request):
    students = Student.objects.all()
    return render(request, 'enroll/students.html', {'students': students})


def studentInfo(request):
    # get data of specific id
    student = Student.objects.get(pk=2)
    print(student)
    return render(request, 'enroll/student.html', {'student': student})
