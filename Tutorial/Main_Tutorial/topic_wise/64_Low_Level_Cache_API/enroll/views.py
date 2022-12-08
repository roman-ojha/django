from django.shortcuts import render

# first import to use per view cache
from django.views.decorators.cache import cache_page


def home(request):
    return render(request, 'enroll/course.html')
