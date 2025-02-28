from rest_framework import serializers

from apps.backend.models.cooperation import Cooperation


class CooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperation
        fields = (
            "id",
            "title",
            "image",
            "created_at",
        )


class CooperationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperation
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
