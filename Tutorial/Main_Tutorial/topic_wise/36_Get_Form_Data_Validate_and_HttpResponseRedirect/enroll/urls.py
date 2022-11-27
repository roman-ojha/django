from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('/success', views.success),
    path('/fail', views.fail)
]
