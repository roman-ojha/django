from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentListView.as_view(), name='student')
]
