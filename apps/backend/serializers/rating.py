from rest_framework import serializers

from apps.backend.models.rating import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
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
