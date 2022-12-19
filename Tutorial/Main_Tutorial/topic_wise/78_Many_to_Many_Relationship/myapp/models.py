from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    # creating many to many relationship with 'User' Model which will create new table by default
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    # because we can't register 'user' into './admin.py' because there could be multiple user
    #  in that case rather then use the 'user' field we will create new function which will return all the user who Sing the song
    def sing_by(self):
        return ",".join([str(p) for p in self.user.all()])
        # return : "roman,razz"
