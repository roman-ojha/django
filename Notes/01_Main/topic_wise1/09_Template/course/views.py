from django.shortcuts import render

from django.http import HttpResponse


def learn_django(request):
    return render(request, 'coursedj.html')


def learn_python(request):
    return render(request, 'coursepy.html')
