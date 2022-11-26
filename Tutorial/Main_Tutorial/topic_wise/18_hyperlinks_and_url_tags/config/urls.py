from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # for application level url we don't need to pass 'name' argument in here but we have to pass 'name' argument inside the application level 'urls.py'
    path('course/', include('course.urls'))
]
