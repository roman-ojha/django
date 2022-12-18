from django.db import models

# create custom manger class


class CustomManager(models.Manager):
    def get_queryset(self):
        # here while we will query to the database using this manager then we want this data to be in order
        return super().get_queryset().order_by('name')
