from django.db import models


class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

    class Meta:
        app_label = 'app'
