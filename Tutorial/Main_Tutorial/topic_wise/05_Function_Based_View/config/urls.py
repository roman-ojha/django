from django.contrib import admin
from django.urls import path

# to import view function we have to first import application view
from course import views

urlpatterns = [
    # root url
    path('', views.index),
    # '/admin' url
    path('admin/', admin.site.urls),
    # '/learndj' url
    path('learndj/', views.learn_django),
    path('learnphp/', views.learn_php),
    path('learnm/', views.learn_math),
]
