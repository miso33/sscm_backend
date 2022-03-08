from rest_framework.generics import ListAPIView

from .models import StudentProfile, Document
from .serializers import DocumentSerializer, StudentReadProfileSerializer
from ..core.permissions import ViewDjangoModelPermission


class DocumentListView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [ViewDjangoModelPermission]


class StudentListView(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentReadProfileSerializer
    permission_classes = [ViewDjangoModelPermission]
