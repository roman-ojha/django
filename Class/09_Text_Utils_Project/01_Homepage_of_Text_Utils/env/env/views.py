from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # render takes three argument one is 'request' and another is the html file in this case index.html and third it take dictionary which dictionary can be able to access by the index.html 


def removepunc(request):
    print(request.GET.get('text','default'))
    # here we will get the data that we send form the textarea and we will get that data as request
    # request.GET.get('<req_vaiable_name>','<default_value>')
    djtext = request.GET.get('text','default')
    return HttpResponse(f"{djtext}")

def capfirst(req):
    return HttpResponse("cap first")

def newlineremove(req):
    return HttpResponse('newline remove')

def spaceremove(req):
    return HttpResponse('spaceremove')

def charcount(req):
    return HttpResponse('charcount')

