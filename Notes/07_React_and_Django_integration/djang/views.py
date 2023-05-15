from django.shortcuts import render
from django.http import HttpResponse


def apiPage(request):
    print("Hello here")
    return HttpResponse("Hello this is from api side")
