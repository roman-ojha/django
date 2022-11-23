from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def learn_django(request):
    # passing date for date & time filter
    date = datetime.now()
    students = {'names': ['roman', 'razz', 'jack', 'harry', 'tom', 'tony']}
    stu = {'stu1': {'name': 'razz', 'roll': 31},
           'stu2': {'name': 'roman', 'roll': 25},
           'stu3': {'name': 'suman', 'roll': 43},
           'stu4': {'name': 'manish', 'roll': 17}
           }
    data = {'cname': 'django', 'duration': "4 Months",
            "seats": 18, 'date': date, 'price': 123.432130, 'students': students, 'stu': stu}
    return render(request, 'course/index.html', context=data)


def learn_python(request):
    data = {'cname': 'python', 'duration': "4 Months", "seats": 18}
    return render(request, 'course/index.html', context=data)
