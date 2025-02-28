from rest_framework import serializers

from apps.backend.models.students import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "title",
            "image",
            "created_at",
        )


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "title",
            "description",
            "description_uz",
            "description_ru",
            "description_en",
            "image",
            "created_at",
        )
