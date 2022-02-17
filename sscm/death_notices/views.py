from rest_framework.generics import CreateAPIView

from sscm.death_notices.models import DeathNotice
from sscm.death_notices.serializers import DeathNoticeSerializer


class DeathNoticeCreateView(CreateAPIView):
    queryset = DeathNotice.objects.all()
    serializer_class = DeathNoticeSerializer
