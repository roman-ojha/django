from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def removepunc(req):
    return HttpResponse("remove punc")

def capfirst(req):
    return HttpResponse("cap first")

def newlineremove(req):
    return HttpResponse('newline remove')

def spaceremove(req):
    return HttpResponse('spaceremove')

def charcount(req):
    return HttpResponse('charcount')

