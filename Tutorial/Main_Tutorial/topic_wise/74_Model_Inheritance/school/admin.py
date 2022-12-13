from django.contrib import admin
from .models import ExamCenter, Student2

# Register your models here.


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']


@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city', 'name', 'roll']
    # we know that this model table don't have field 'id', 'cname', 'city'
    # but also we can access these field inside this model because we have inherited from 'ExamCenter' model
    # and if you will try to insert data into 'Student2' it will also insert new data into 'ExamCenter'
