from django.db import models

# Create your models here.


class Tweet(models.Model):
    context = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)
    # blank means not required in djano and also not require in database
