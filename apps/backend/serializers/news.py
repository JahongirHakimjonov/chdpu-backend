from rest_framework import serializers

from apps.backend.models.news import News, NewsCategory


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "image",
            "category",
            "created_at",
        )


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "image",
            "description",
            "created_at",
        )


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = (
            "id",
            "name",
        )
