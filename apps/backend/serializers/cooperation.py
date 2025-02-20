from rest_framework import serializers

from apps.backend.models.cooperation import Cooperation


class CooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperation
        fields = (
            "id",
            "title",
            "description",
            "image",
            "created_at",
        )
