from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('course/', views.home),
]
