from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Home Page</h1>")
    # here this function will run and response the given string to that url

def about(request):
    return HttpResponse("about page")
