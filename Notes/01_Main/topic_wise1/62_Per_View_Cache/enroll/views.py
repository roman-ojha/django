from django.shortcuts import render

# first import to use per view cache
from django.views.decorators.cache import cache_page


@cache_page(20)
# caching home page
# @cache_page(<timeout>)
def home(request):
    return render(request, 'enroll/course.html')


def contact(request):
    return render(request, 'enroll/contact.html')
