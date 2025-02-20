from rest_framework import serializers

from apps.backend.models.info import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = (
            "id",
            "title",
            "description",
            "image",
            "created_at",
        )
