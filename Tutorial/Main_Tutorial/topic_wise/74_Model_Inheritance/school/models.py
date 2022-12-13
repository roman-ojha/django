from django.db import models


# Creating Base class model
# here for this class we don't want to create a table on database because of that we will create this class as abstract base class
class CommonInfo(models.Model):
    # adding common filed that we might use on child class
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()

    # creating this class as abstract base class
    class Meta:
        abstract = True


class Student(CommonInfo):
    # name = models.CharField(max_length=70)
    # age = models.IntegerField()
    fees = models.IntegerField()

    # we don't want 'date' filed in the 'Student' Model/Table in that case we will assign None
    date = None


class Teacher(CommonInfo):
    # name = models.CharField(max_length=70)
    # age = models.IntegerField()
    # date = models.DateField()
    salary = models.IntegerField()


class Contractor(CommonInfo):
    # name = models.CharField(max_length=70)
    # age = models.IntegerField()

    # overriding 'date' field from base class
    date = models.DateTimeField()
    salary = models.IntegerField()
