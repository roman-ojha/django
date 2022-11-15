from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={
        "name":"roman",
        "place":"earth",
    }
    return render(request,'index.html',params)
    # render takes three argument one is 'request' and another is the html file in this case index.html and third it take dictionary which dictionary can be able to access by the index.html 