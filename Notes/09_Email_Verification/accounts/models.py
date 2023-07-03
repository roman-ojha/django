from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # one to one relation with user
    auth_token = models.CharField(max_length=100)
    # token that we will use to verify the user where we pass verification url for the given user email then we will going to search the user according to the token provide from the url then we will verify the user
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
