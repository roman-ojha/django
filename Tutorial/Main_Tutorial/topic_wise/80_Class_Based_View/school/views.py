from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm


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
def homeFunc(request):
    context = {'from': "Function Based View"}
    return render(request, 'school/home.html', context)


# Class Based View return 'render' function
class HomeClass(View):
    def get(self, request):
        context = {'from': "Class Based View"}
        return render(request, 'school/home.html', context)


# Function Based View using Forms
def contactFun(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Form submitted')
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form': form})


# Class Based View using Forms
class ContactClass(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Form submitted')
        else:
            return HttpResponse("Invalid Form")
