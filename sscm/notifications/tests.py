import pytest
from django.db.models import F
from django.test import TestCase
from .models import Notification
from .factories import NotificationFactory
from .tasks import send_emails


class EmailTestCase(TestCase):

    @pytest.mark.email
    def test_send(self):
        NotificationFactory.create_batch(
            10,
            channel="EMAIL",

        )
        send_emails()
        self.assertFalse(Notification.objects.filter(sent=False).count())

    @pytest.mark.email
    def test_set_channel(self):
        NotificationFactory.create_batch(
            10,
            channel="EMAIL",
        )
        NotificationFactory.create_batch(
            10,
            channel="FIREBASE",
        )
        send_emails()
        self.assertFalse(Notification.objects.filter(sent=False, channel="EMAIL").count())
        self.assertEqual(
            Notification.objects.filter(sent=False, channel="FIREBASE").count(),
            Notification.objects.filter(channel="FIREBASE").count()
        )

    @pytest.mark.email
    def test_set_attempts_number(self):
        NotificationFactory.create_batch(
            3,
            channel="EMAIL",
        )
        NotificationFactory.create_batch(
            3,
            channel="EMAIL",
            attempts_max=10,
            attempts_number=10
        )
        NotificationFactory.create_batch(
            3,
            channel="EMAIL",
            attempts_max=10,
            attempts_number=20
        )
        send_emails()
        self.assertEqual(
            Notification.objects.filter(
                attempts_max__gt=F('attempts_number'),
            ).count(),
            Notification.objects.filter(
                sent=True
            ).count()
        )

    @pytest.mark.skip(reason="")
    def test_set_last_attempt(self):
        self.assertTrue(True)

    @pytest.mark.skip(reason="")
    def test_set_sent_datetime(self):
        NotificationFactory()
        self.assertTrue(True)

    @pytest.mark.skip(reason="")
    def test_set_sent(self):
        NotificationFactory()
        self.assertTrue(True)
        # Notification.objects.create(
        #
        # )

    @pytest.mark.skip(reason="")
    def test_check_max_attempts(self):
        NotificationFactory()
        self.assertTrue(True)

    @pytest.mark.skip(reason="")
    def test_check_sent(self):
        NotificationFactory()
        self.assertTrue(True)

    def test_send_schedule(self):
        NotificationFactory()
        self.assertTrue(True)
