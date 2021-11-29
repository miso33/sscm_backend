from drf_recaptcha.fields import ReCaptchaV3Field
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView


class V3Serializer(Serializer):
    recaptcha = ReCaptchaV3Field(action="login")


class GetOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = V3Serializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            return Response({}, status=status.HTTP_200_OK)
        return Response({"captcha": "Verifikácia pomocou reCaptcha zlyhala!"}, status=status.HTTP_400_BAD_REQUEST)