from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    # One to One relationship
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_published_date = models.DateField()


class Post(models.Model):
    # Many to one relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_published_date = models.DateField(max_length=70)


class Song(models.Model):
    # Many to many relationship
    user = models.ManyToManyField(User, related_name='mysong')
    # if we will give 'related_name' then it means that while querying the data for song related data in that case we have to use 'mysong'
    # EX: User.objects.filter(mysong__song_duration=32)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def sing_by(self):
        return ",".join([str(p) for p in self.user.all()])
