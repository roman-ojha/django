from django.shortcuts import render
from django.http import HttpResponse


def fees_django(request):
    price = {'price': 400}
    return render(request, 'fees/django.html', context=price)


def fees_python(request):
    price = {'price': 300}
    return render(request, 'fees/python.html', context=price)
