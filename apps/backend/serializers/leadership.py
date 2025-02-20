from rest_framework import serializers

from apps.backend.models.leadership import Leadership


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = (
            "id",
            "name",
            "title",
            "description",
            "image",
            "created_at",
        )
