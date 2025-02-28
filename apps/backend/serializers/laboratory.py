from rest_framework import serializers

from apps.backend.models.laboratory import Laboratory, LaboratoryGallery


class LaboratoryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryGallery
        fields = (
            "id",
            "image",
            "created_at",
        )


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = (
            "id",
            "title",
            "image",
            "created_at",
        )


class LaboratoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["gallery"] = LaboratoryGallerySerializer(
            instance.laboratory_galleries.all(), many=True
        ).data
        return data
