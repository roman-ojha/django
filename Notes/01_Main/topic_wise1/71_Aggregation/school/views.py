from django.shortcuts import render
from .models import Student

# first we will import aggregation function
from django.db.models import Avg, Sum, Min, Max, Count


def home(request):
    students = Student.objects.all()

    # getting average of marks
    average = students.aggregate(Avg('marks'))
    print(average)

    # getting sum of marks
    sum = students.aggregate(Sum('marks'))
    print(sum)

    # getting min of marks
    min = students.aggregate(Min('marks'))
    print(min)

    # getting max of marks
    max = students.aggregate(Max('marks'))
    print(max)

    # getting count of marks
    count = students.aggregate(Count('marks'))
    print(count)
    return render(request, 'school/home.html')
