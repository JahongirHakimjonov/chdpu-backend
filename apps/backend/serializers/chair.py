from rest_framework import serializers

from apps.backend.models.chair import Chair, ChairMember


class ChairMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChairMember
        fields = (
            "id",
            "chair",
            "name",
            "title",
            "image",
            "created_at",
        )


class ChairMemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChairMember
        fields = (
            "id",
            "chair",
            "name",
            "title",
            "description",
            "description_uz",
            "description_ru",
            "description_en",
            "image",
            "created_at",
        )


class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = (
            "id",
            "name",
            "title",
            "image",
            "created_at",
        )


class ChairDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = (
            "id",
            "name",
            "title",
            "description",
            "description_uz",
            "description_ru",
            "description_en",
            "image",
            "created_at",
        )
