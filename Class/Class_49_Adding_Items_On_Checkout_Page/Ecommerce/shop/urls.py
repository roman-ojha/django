from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrakingStatus"),
    path('search/', views.search, name="Search"),
    path('products/<int:myid>', views.productview, name="ProductView"),
    # here id will be the params when will be request by the user
    # now we can get the value of id and operate in views.py
    path('checkout/', views.checkout, name="Checkout"),
]
