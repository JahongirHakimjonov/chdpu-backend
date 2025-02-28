from rest_framework import serializers

from apps.backend.models.info import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = (
            "id",
            "title",
            "image",
            "created_at",
        )


class InfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
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
