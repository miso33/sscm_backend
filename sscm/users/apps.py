from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "sscm.users"
    verbose_name = "Používatelia"

    def ready(self):
        import sscm.users.signals
