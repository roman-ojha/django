from django.shortcuts import render
from .models import Student
from django.db.models import Q


def home(request):
    students = Student.objects.filter(Q(id=2) & Q(roll=30))
    # here we want record having both id having 2 and roll having 30
    print(students)

    students = Student.objects.filter(Q(id=2) | Q(marks=300))
    # here we want record having whether id 2 and roll 30
    print(students)

    students = Student.objects.filter(~Q(id=2))
    # here we want record which don't have id 2
    print(students)
    return render(request, 'school/home.html')
