from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from .models import Student, School


class StudentSerializer(ModelSerializer):
    home_school = CharField(source="home_school.name")
    foreign_school = CharField(source="foreign_school.name")

    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'academic_year',
            'semester',
            'home_school',
            'foreign_school',
        ]
