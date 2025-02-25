from rest_framework import serializers

from apps.backend.models.laboratory import Laboratory


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = (
            "id",
            "title",
            "description",
            "image",
            "created_at",
        )
