from django.db import models


# first we will create a model and the register it into 'admin.py'
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
