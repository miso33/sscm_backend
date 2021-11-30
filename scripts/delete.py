from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


def run():
    OutstandingToken.objects.filter(user__email='labas@scrypta.sk').delete()
