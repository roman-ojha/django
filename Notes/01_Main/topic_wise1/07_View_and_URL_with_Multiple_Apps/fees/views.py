from django.shortcuts import render

from django.http import HttpResponse


def fees_django(request):
    return HttpResponse("<h1> Fees Django </h1>")
