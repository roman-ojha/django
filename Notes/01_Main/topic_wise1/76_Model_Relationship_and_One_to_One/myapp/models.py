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

    # Now when we will delete the user then it will delete the Page as well on by default
    # But if we will delete  the page then it will not delete the user
    # To make that happen we can create a signal which will delete the user whenever we will delete the page associated with it
    # we will create signal on './signals.py'


# One-to-One relationship using Model Inheritance
class Like(Page):
    # here when we will inherit new model with the existing model then automatically there will be one-to-one relationship with these two model

    # But rather then using the default behavior we want our own relationship to the 'Page' Model in that case we will do this:
    page = models.OneToOneField(
        Page, on_delete=models.CASCADE, primary_key=True,
        # we also have to add 'parent_link' True
        parent_link=True)

    likes = models.IntegerField()

    # Now while adding new Like we will get all the file relate to 'Page' & 'Like' Model
