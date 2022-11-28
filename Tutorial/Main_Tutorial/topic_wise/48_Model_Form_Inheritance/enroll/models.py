from django.db import models


class User(models.Model):
    student_name = models.CharField(max_length=70, blank=True)
    teacher_name = models.CharField(max_length=70, blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
