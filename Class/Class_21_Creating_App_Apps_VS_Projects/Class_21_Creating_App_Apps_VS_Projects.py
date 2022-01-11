"""
-> we can have multiple apps in a project
-> we can have a app in multiple project
App is the plugable web application

-> so we can make a multiple apps in a project
-> so first rather then running server 
-> wirte' python manage.py startapp <app_name> 'in django environment
-> 'app_name' in this case is 'shop'
-> and write ' python manage.py startapp blog ' to make another app in the same project

-> now inside the shop folder you have to make 'urls.py'
-> now add in 'urls.py'
            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.index, name="shopHome")
            ]
-> but we also have to put to the main 'env' folder url.py file
-> now add in 'env' folder 'url.py' file:
            from django.contrib import admin
            from django.urls import path, include
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('shop/', include('shop.urls'))
                # here first django project will run and after that when the use go to the 'shop/' url
                # at that time it will push that in the shop app 'shop.urls'
            ]
-> now do the exact same thing for the blog application
-> and wirte the code as per the project app of the shop
"""