from django.conf import settings
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import User
from ..exchanges.models import StudentProfile
from ..notifications.models import Notification
from ..profiles.models import IndividualProfile, GroupProfile


# @receiver(pre_save, sender=User)
# def add_user_to_public_group(sender, instance, *args, **kwargs):
#     try:
#         volunteer_group = Group.objects.get(name="volunteer")
#         if hasattr(instance, "volunteer_profile") and volunteer_group not in instance.groups.all():
#             instance.groups.add(volunteer_group)
#         if hasattr(instance, "name"):
#             instance.groups.add(Group.objects.get(name="organization"))
#
#     except ObjectDoesNotExist as error:
#         logger.exception(error)

@receiver(post_save, sender=IndividualProfile)
def add_individual(sender, instance, created, *args, **kwargs):
    if created and instance.user is not None:
        Notification.objects.create(
            recipients=["info@sscm.sk", "cyrilametod.sk@gmail.com", "annasevkova@azet.sk"],
            body=f"Užívateľ: {instance.first_name} {instance.last_name} ({instance.user.email}) bol úspešne " \
                 f"zaregistrovaný."
        )


@receiver(post_save, sender=GroupProfile)
def add_group(sender, instance, created, *args, **kwargs):
    if created and instance.user is not None:
        Notification.objects.create(
            recipients=["info@sscm.sk", "cyrilametod.sk@gmail.com", "annasevkova@azet.sk"],
            body=f"""
                    Skupina: {instance.name} ({instance.user.email})
                    bola úspešne zaregistrovaná.
                 """
        )
