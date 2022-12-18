from django.db import models

# create custom manger class


class CustomManager(models.Manager):
    def get_queryset(self):
        # here while we will query to the database using this manager then we want this data to be in order
        return super().get_queryset().order_by('name')

    # creating custom manager method
    def get_stu_roll_range(self, r1, r2):
        # in this method we will take range 1 'r1' & range 2 'r2' and query according to that
        return super().get_queryset().filter(roll__range=(r1, r2))
        # returning only those student whose roll no from 'r1'-'r2'
