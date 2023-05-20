from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=250, help_text="This is title title")
    content = models.TextField(default=None, blank=True)

    def __str__(self) -> str:
        return self.title
