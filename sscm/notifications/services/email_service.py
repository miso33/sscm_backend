from datetime import datetime

from django.conf import settings
from django.core import mail

from sscm.notifications.services.notification_service import NotificationService


class EmailsService(NotificationService):
    email_message = None
    email = None
    channel = "EMAIL"

    def before_send(self):

        self.email.attempts_number += 1
        self.email.last_attempt = datetime.now()
        self.email.save()

    def create_email_message(self, connection):
        self.email_message = mail.EmailMessage(
            self.email.subject,
            self.email.body,
            settings.EMAIL_HOST_USER,
            self.email.recipients,
            connection=connection,
        )
        # self.email_message.content_subtype = "html"

    def send(self):
        return self.email_message.send()

    def after_send(self, sent):
        if sent:
            self.email.sent_datetime = datetime.now()
            self.email.sent = True
            self.email.save()

    def attachment(self):
        if self.email.attachment_file:
            pass

    def email_processing(self, emails_per_connection):

        with mail.get_connection() as connection:
            for email in self.get_notifications_list(notifications_per_connection=emails_per_connection):
                self.email = email
                self.before_send()
                self.create_email_message(connection)
                self.attachment()
                sent = self.send()
                self.after_send(sent)
