from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    # fetching all the product from the database
    products = Product.objects.all()
    print(products)
    # getting the number of slide:
    n = len(products)
    nSlides = n//4+ceil((n/4)-(n//4))

    params = {'no_of_slides': nSlides,
              'range': range(1, nSlides), 'product': products}
    # here we are putting range function inside the params because we can use the value of this which return the generator
    # after rendering the index.html inside there will call all parameter or params value
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("we are at contact")


def tracker(request):
    return HttpResponse("we are at traker")


def search(request):
    return HttpResponse("we are at search")


def productview(request):
    return HttpResponse("we are at productview")


def checkout(request):
    return HttpResponse("we are at checkout")
