from rest_framework import serializers

from apps.backend.models.admission import Admission


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = (
            "id",
            "title",
            "image",
            "created_at",
        )


class AdmissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = (
            "id",
            "title",
            "image",
            "description",
            "description_uz",
            "description_ru",
            "description_en",
            "created_at",
        )
