from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video
from .permissions import CanWatchMovie


class CodeView(APIView):
    permission_classes = [CanWatchMovie]

    def get(self, request):
        video = Video.objects.last()
        if video:
            return Response({"code": video.code}, status=status.HTTP_200_OK)
        return Response(
            {"code": "Not Found"},
            status=status.HTTP_404_NOT_FOUND,
        )
