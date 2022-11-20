from django.shortcuts import render

from django.http import HttpResponse


def learn_django(request):
    data = {'cname': 'django', 'duration': "4 Months", "seats": 18}
    return render(request, 'course/index.html', context=data)


def learn_python(request):
    data = {'cname': 'python', 'duration': "4 Months", "seats": 18}
    return render(request, 'course/index.html', context=data)
