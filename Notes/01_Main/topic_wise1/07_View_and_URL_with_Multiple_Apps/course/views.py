from django.shortcuts import render

from django.http import HttpResponse


def learn_django(request):
    return HttpResponse("<h1> Learn Django </h1>")
