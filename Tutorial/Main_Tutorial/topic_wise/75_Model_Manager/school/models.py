from django.db import models
from .manager import CustomManager


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # you can change the manager name by default it is 'objects'
    students = models.Manager()

    # using custom manager now we can use this manager as well to access the querySet
    students_custom = CustomManager()
