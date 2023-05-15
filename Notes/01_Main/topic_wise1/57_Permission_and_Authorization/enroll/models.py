from django.db import models

# now here we will create a new model
# we know that every time we create a new model django will automatically create 4 permission for that model
# to 'change', 'view', 'delete', 'add'


class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
