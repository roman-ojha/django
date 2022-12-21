from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Function based view
def myView(request):
    return HttpResponse("Function based view")


# Class Based View
# Extend from 'View'
class MyView(View):
    get_data = ""

    # For GET Method
    def get(self, request):
        # return HttpResponse("Class based view - GET")
        # accessing object property
        return HttpResponse(self.get_data)


# We can create a child class using 'MyView' class and inherit the functionality of parent
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.get_data)

# Function Based View return 'render' function
# def homeFunc(request):
#     return render(request,'')
