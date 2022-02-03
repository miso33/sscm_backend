from sscm.core.views import BaseListView
from .models import Student
from .serializers import StudentSerializer


class StudentListView(BaseListView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
