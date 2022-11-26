from django.urls import path
from . import views

urlpatterns = [
    path('dj/', views.learn_django, name='django_course')
]
