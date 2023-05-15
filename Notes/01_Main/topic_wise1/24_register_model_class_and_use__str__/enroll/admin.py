from django.contrib import admin

# first we will import the model class
from .models import Student

# Register your models here.
admin.site.register(Student)
