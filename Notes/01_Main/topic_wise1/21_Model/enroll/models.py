from django.db import models


class Student(models.Model):
    # stuid = models.IntegerField(primary_key=True)
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)
    comment = models.CharField(max_length=100, default='Not Available')
