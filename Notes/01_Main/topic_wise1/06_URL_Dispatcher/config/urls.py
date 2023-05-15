from django.contrib import admin
from django.urls import path

from course import views

urlpatterns = [
    # root url
    path('', views.index),
    # '/admin' url
    path('admin/', admin.site.urls),
    # '/learndj' url
    path('learndj/', views.learn_django),
    path('altlearnphp/', views.learn_django),
]
