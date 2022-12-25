from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.CreateStudentView.as_view(), name='create'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thanks'),
    path('update/<int:pk>', views.UpdateStudentView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteStudentView.as_view(), name='delete')
]
