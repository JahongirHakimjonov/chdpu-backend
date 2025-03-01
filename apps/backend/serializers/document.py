from rest_framework import serializers

from apps.backend.models.document import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
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
