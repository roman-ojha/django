from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    # products = Product.objects.all()
    # print(products)
    #  n = len(products)
    #         nSlides = n//4+ceil((n/4)-(n//4))
    # allProds = [[products, range(1, nSlides), nSlides], [
    #     products, range(1, nSlides), nSlides]]
    allProds = []
    catprods = Product.objects.values('category', 'id')
    # here we are getting the 'category' and 'id' of the product form the database
    cats = {item['category'] for item in catprods}
    # now here we will get all the category from the 'catprods'
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        # here we are getting the product which category same as the cat
        n = len(prod)
        nSlides = n//4+ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
        # now we will append all of the product in allProds
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productview(request):
    return render(request, 'shop/prodView.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
