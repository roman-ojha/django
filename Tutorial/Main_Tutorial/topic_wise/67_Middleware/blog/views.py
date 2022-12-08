from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


def home(request):

    # throwing exception for 'process_exception' middleware hook method
    # a = 10/0

    print("This is from View")
    # return HttpResponse("Home Page")

    # Example for 'process_template_response' middleware hooke method
    # returning template response
    return TemplateResponse(request, 'blog/user.html', {'name': 'Roman'})
    # we have response with the context with certain value but if you want to manipulate these template response context the we can use 'process_template_response' middleware hook method
