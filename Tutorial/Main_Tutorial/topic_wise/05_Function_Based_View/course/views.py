from django.shortcuts import render

# import HttpResponse first
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home Page")


def learn_django(request):
    # view function take 'request' object as params

    return HttpResponse('<h1> Hello Django </h1>')


def learn_php(request):
    return HttpResponse('<h1> Hello PHP </h1>')


def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)
