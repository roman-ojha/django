from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.CreateStudentView.as_view(), name='create'),
    path('thanks/', views.ThankTemplateView.as_view(), name='thanks'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student'),
]
