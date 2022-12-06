from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setCookie),
    path('get/', views.getCookie),
    path('del/', views.deleteCookie),
    path('set/signed/', views.setSignedCookies),
    path('get/signed/', views.getSignedCookies),
]
