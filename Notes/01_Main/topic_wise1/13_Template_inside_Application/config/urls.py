from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # one way to use view.py inside project folder
    # path('', views.home),
    # another way to use 'views.py' file for project related stuff
    path('', include('core.urls')),
    path('course/', include('course.urls')),
    path('fees/', include('fees.urls')),
]
