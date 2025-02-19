from rest_framework import serializers

from apps.backend.models.students import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
