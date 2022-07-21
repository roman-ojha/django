from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),
    path('', include('django.contrib.auth.urls'))
    # so these are bunch of pre-build urls that will automatically do things like login, logout, password reset
    # and you need to write html template to allow this to work
    # so inside the 'myApp/templates/registration' we will create 'login.html'
    # and now that will happen is that login root that is provided by the django will automatically render this login page whenever user will go to the url '/login'
    # NOTE: the template needs to be inside the registration folder
]
