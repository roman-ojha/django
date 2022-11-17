from django.contrib import admin
from django.urls import path

from course import views as courseViews
from fees.views import fees_django

urlpatterns = [
    path('admin/', admin.site.urls),
]
