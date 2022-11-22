from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def learn_django(request):
    # passing date for date & time filter
    date = datetime.now()
    data = {'cname': 'django', 'duration': "4 Months",
            "seats": 18, 'date': date, 'price': 123.432130}
    return render(request, 'course/index.html', context=data)


def learn_python(request):
    data = {'cname': 'python', 'duration': "4 Months", "seats": 18}
    return render(request, 'course/index.html', context=data)
