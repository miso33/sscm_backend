from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


def run():
    OutstandingToken.objects.filter(
        user__email_in=[
            "domestro@outlook.com",
            "hospodar@saske.sk",
            "info@scrypta.sk",
            "jozefma1k@scrypta.sk",
            "mark.varchola@gmail.com",
            "mark.varchola+1@gmail.com",
            "mgacko@gmail.com",
            "mkogaci@gmail.com"
        ]
    ).delete()
