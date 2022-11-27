from django.db import models


class User(models.Model):
    name = models.CharField(max_length=70, blank=True)
    # blank = True (Model form for this field will be required False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
