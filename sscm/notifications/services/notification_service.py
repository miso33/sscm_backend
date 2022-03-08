from datetime import datetime

from django.db.models import F

from sscm.notifications.models import Notification


class NotificationService:

    def get_notifications_list(self, notifications_per_connection=10):
        return Notification.objects.filter(
            send_schedule__lte=datetime.now(),
            attempts_max__gt=F('attempts_number'),
            sent=False,
            channel=self.channel
        )[:notifications_per_connection]
