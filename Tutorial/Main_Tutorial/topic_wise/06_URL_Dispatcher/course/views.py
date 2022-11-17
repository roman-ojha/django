from django.shortcuts import render

# import HttpResponse first
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home Page")


def learn_django(request):
    return HttpResponse('<h1> Hello Django </h1>')
