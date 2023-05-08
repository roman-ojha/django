from django.urls import path
from controller import register

urlpatterns = [
    path('register/', register.register),
]
