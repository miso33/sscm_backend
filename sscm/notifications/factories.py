import factory
from faker import Faker
from datetime import datetime, timedelta
from .models import Notification

fake = Faker()


class NotificationFactory(factory.django.DjangoModelFactory):
    recipients = [fake.email() for _ in range(0, 5)]
    recipients_copy = None
    recipients_blind_copy = None
    subject = fake.bothify(text='Subject: ########')
    body = fake.bothify(text='########')
    body_raw = ""
    attachment_file = None
    send_schedule = datetime.now()
    attempts_max = 10
    attempts_number = 0
    last_attempt = None
    sent_datetime = None
    sent = False
    channel = fake.random_element(elements=('EMAIL', 'FIREBASE'))

    class Meta:
        model = Notification
