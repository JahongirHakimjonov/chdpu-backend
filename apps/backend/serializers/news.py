from rest_framework import serializers

from apps.backend.models.news import News, NewsCategory


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = (
            "id",
            "name",
        )


class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer()

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
    category = NewsCategorySerializer()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "image",
            "description",
            "category",
            "created_at",
        )
