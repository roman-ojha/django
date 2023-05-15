from django.contrib import admin
from .models import Student, Student2, ProxyStudent

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(ProxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']
