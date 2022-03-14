from django.urls import path

from .views import StudentListView, DocumentListView

urlpatterns = [
    path('student/', StudentListView.as_view(), name="student-list"),
    path('document/', DocumentListView.as_view(), name="document-list"),
]
