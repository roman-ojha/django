from .models import Page
from django.db.models.signals import post_delete
# we need post_delete signal for this example
from django.dispatch import receiver


@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    print("Page Post_Delete")

    # deleting user data after we delete page data
    instance.user.delete()
