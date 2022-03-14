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
# def my_callback(sender, instance, *args, **kwargs):
#     print("post_save user")
#
#
# @receiver(post_save, sender=StudentProfile)
# def my_callback(sender, instance, *args, **kwargs):
#     print("post_save")
#
#
# @receiver(pre_save, sender=StudentProfile)
# def my_callback(sender, instance, *args, **kwargs):
#     print("SIGNAL")
#     try:
#         old_student_profile = StudentProfile.objects.get(id=instance.id)
#         # print(instance.user.type == User.Types.EXCHANGE)
#         # print(old_student_profile.parish)
#         if instance.user.type == User.Types.EXCHANGE and not old_student_profile.parish:
#             # print("tunak")
#             instance.user.type = User.Types.MEMBER
#             instance.status = StudentProfile.Status.ACTIVE
#     except ObjectDoesNotExist:
#         # print("ObjectDoesNotExist")
#         pass
#

@receiver(post_save, sender=IndividualProfile)
def my_callback(sender, instance, created, *args, **kwargs):
    if created and hasattr(instance, 'user'):
        Notification.objects.create(
            recipients=[settings.EMAIL_HOST_USER],
            body=f"Užívateľ: {instance.first_name} {instance.last_name} ({instance.user.email}) bol úspešne " \
                 f"zaregistrovaný."
        )


@receiver(post_save, sender=GroupProfile)
def my_callback(sender, instance, created, *args, **kwargs):
    if created:
        Notification.objects.create(
            recipients=[settings.EMAIL_HOST_USER],
            body=f"""
                    Skupina: {instance.name} ({instance.user.email})
                    bola úspešne zaregistrovaná.
                 """
        )
