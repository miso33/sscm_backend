from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video
from .permissions import CanWatchMovie


class CodeView(APIView):
    permission_classes = [CanWatchMovie]

    def get(self, request):
        video = Video.objects.first()
        if video:
            return Response({"code": video.code}, status=status.HTTP_200_OK)
        return Response(
            {"code": None},
            status=status.HTTP_400_BAD_REQUEST,
        )
