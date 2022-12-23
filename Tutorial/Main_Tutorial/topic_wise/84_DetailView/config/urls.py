from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Passing pk dynamic value from url to 'DetailView' class
    path('student/<int:id>', views.StudentDetailView.as_view(), name='student'),

    path('student/', views.StudentListView.as_view(), name='students')
]
