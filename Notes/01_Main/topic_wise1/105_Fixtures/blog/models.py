from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self):
        return self.title
