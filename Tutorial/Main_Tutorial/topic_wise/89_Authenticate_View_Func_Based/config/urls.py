from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # here we just have to give now url path which will include every authentication url path with it's implemented view function
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("registration.urls")),
]
