from rest_framework import serializers

from apps.backend.models.news import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "description",
            "image",
            "created_at",
        )
