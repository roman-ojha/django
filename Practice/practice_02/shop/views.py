from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Shop")


def about(request):
    return HttpResponse("we are at about")


def contact(request):
    return HttpResponse("we are at contact")


def tracker(request):
    return HttpResponse("we are at traker")


def search(request):
    return HttpResponse("we are at search")


def productview(request):
    return HttpResponse("we are at productview")


def checkout(request):
    return HttpResponse("we are at checkout")
