from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # you can change the manager name by default it is 'objects'
    objects = models.Manager()
