from rest_framework import serializers

from apps.backend.models.buildings import Building, BuildingGallery


class BuildingGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingGallery
        fields = (
            "id",
            "image",
            "created_at",
        )


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = (
            "id",
            "title",
            "image",
            "description",
            "description_uz",
            "description_ru",
            "description_en",
            "created_at",
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["gallery"] = BuildingGallerySerializer(
            instance.gallery.all(), many=True
        ).data
        return response
