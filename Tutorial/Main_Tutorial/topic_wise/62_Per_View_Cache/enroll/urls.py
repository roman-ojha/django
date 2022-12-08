from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('course/', views.home),

    # cache using url
    # NOTE: cache will be different for every dynamic url value if it exist
    path('contact/', cache_page(10)(views.contact)),
]
