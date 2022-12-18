from django.db import models
from .manager import CustomManager


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # you can change the manager name by default it is 'objects'
    students = models.Manager()

    # using custom manager now we can use this manager as well to access the querySet
    students_custom = CustomManager()


# Example to implement Model Manager with Proxy Model
class Student2(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

# Creating Proxy model


class ProxyStudent(Student2):
    # Creating proxy model for 'Student2' table
    class Meta:
        proxy = True
        # changing order behavior
        ordering = ['name']
    # using custom manager for the proxy model
    students_custom = CustomManager()
