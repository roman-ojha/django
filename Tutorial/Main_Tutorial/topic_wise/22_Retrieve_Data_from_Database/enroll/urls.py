from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsInfo),
    path('student/', views.studentInfo),
]
