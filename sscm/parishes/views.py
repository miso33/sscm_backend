from rest_framework import generics
from rest_framework.permissions import AllowAny

from sscm.parishes.models import Parish
from sscm.parishes.serializers import ParishSerializer


class ParishList(generics.ListAPIView):
    queryset = Parish.objects.all()
    serializer_class = ParishSerializer
    permission_classes = [AllowAny]
