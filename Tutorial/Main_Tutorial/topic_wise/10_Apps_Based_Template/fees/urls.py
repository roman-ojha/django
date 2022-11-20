from django.urls import path
from . import views

urlpatterns = [
    path('dj/', views.fees_django),
    path('py/', views.fees_python)
]
