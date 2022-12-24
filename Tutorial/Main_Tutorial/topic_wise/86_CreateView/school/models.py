from django.db import models
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)

    def get_absolute_url(self):
        # we can also define the success_url that we define inside 'CreateView' to get redirect into the given url after it form get save into database

        # redirect to '/thanks' url
        # return reverse('thanks')

        # but we will redirect to the dynamic url to show the student after he/she created it
        return reverse("student", kwargs={'pk': self.pk})
