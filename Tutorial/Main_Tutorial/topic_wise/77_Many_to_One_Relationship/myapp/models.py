from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # creating many to one relation with 'User' Model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_published_date = models.DateField(max_length=70)
