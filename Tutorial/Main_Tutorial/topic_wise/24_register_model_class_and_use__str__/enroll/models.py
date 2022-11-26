from django.db import models


class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)

    def __str__(self) -> str:
        # we will return the filed that we want to see on django admin interface

        # return self.stuname
        return f"{self.stuid} {self.stuname}"
        # EX: 102 harry
