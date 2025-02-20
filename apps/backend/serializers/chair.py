from rest_framework import serializers

from apps.backend.models.chair import Chair


class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = (
            "id",
            "name",
            "title",
            "description",
            "image",
            "created_at",
        )
