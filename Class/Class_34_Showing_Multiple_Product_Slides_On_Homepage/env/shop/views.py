from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4+ceil((n/4)-(n//4))
    # here we will going to create the all Product List inside we will categorize with There another list
    allProds = [[products, range(1, nSlides), nSlides], [
        products, range(1, nSlides), nSlides]]
    # and after that we will pass the allProds as the params
    params = {'allProds': allProds}
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
