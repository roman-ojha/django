from django.shortcuts import render
from django.http import HttpResponse


def fees_django(request):
    return render(request, 'feesdj.html')


def fees_python(request):
    return render(request, 'feespy.html')
