from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from .models import StudentProfile, Document
from ..profiles.serializers import MemberProfileSerializer


class StudentReadProfileSerializer(ModelSerializer):
    home_school = CharField(source="home_school.name", read_only=True)
    foreign_school = CharField(source="foreign_school.name", read_only=True)

    class Meta:
        model = StudentProfile
        fields = [
            'first_name',
            'last_name',
            'academic_year',
            'semester',
            'home_school',
            'foreign_school',
        ]


class StudentProfileSerializer(MemberProfileSerializer):
    class Meta:
        model = StudentProfile
        fields = [
                     'first_name',
                     'last_name',
                     'birth_date',
                     'profession',
                     'title_prefix',
                     'title_suffix',
                 ] + MemberProfileSerializer.Meta.fields


class DocumentSerializer(ModelSerializer):
    document = CharField(source="document.url", read_only=True)

    class Meta:
        model = Document
        fields = [
            'document',
        ]
