from celery import shared_task

from sscm.notifications.services.email_service import EmailsService


@shared_task(name='send_emails')
def send_emails(emails_per_connection=10):
    EmailsService().email_processing(emails_per_connection=emails_per_connection)
