from django.db import models

# we will use django built in default 'User' Model
from django.contrib.auth.models import User


class Page(models.Model):
    # creating one-to-one relation with 'User' model
    # also we used 'user' field as primary key as well
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(
    #     User, on_delete=models.PROTECT, primary_key=True)

    # if you want to create page only for particular person then you can limit for those one
    # in this case only staff member can have Page
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})

    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_published_date = models.DateField()
