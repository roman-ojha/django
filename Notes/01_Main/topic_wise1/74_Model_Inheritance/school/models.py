from django.db import models


# Abstract base class Inheritance: ========================================
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


# Multi table Inheritance: ========================================
# https://youtu.be/cg9pb6V7IQk?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&t=2541
class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    # field for this table are 'id', 'cname', 'city'


class Student2(ExamCenter):
    # here if we inherit from Base class then it will create the one to one relation with the base class
    # means inside Student2 Table it will automatically create new field which will make relation with the base class
    # in this case it will create a field called 'examcenter_ptr_id' inside this Model table
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # field for this table are 'examcenter_ptr_id', 'name', 'roll'


#  Proxy Model: ========================================
class ExamCenter2(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)


class MyExampleCenter(ExamCenter2):
    class Meta:
        # creating proxy model using 'ExamCenter2'
        proxy = True
        # because we create the proxy model from 'ExamCenter2' django will only create the table for 'ExamCenter2' model
        # but there will exist the proxy of that base class model

        # now if we will add a new data from any of these two model till will get save into one table

        # now inside the proxy model we can change the behavior of the model

        # like the ordering
        ordering = ['id']
        # now the order of the field inside 'MyExampleCenter' will be 1, 2, 3, 4
        # but the default order on 'ExamCenter2' will be 4, 3, 2, 1

        # ordering using city
        # ordering = ['city']
