from django.shortcuts import render
from .models import Student

# Create your views here.


def home(request):
    # Getting all the data from table
    students = Student.objects.all()
    print(students)
    # if you want to see the SQL query that this method is generating then you can use this:
    print("SQL Query: ", students.query)

    # Filter method to return by passing parameters
    students = Student.objects.filter(marks=300)
    # getting all the student whose marks is 300

    # Exclude
    students = Student.objects.exclude(marks=300)
    # getting all the student whose marks is not 300

    # OrderBy
    return render(request, 'school/home.html', {'students': students})
