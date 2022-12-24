from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.CreateStudentView.as_view(), name='create')
]
