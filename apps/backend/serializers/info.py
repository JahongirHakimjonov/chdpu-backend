from rest_framework import serializers

from apps.backend.models.info import Info, InfoContact


class InfoContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoContact
        fields = (
            "id",
            "info",
            "contact_type",
            "value",
            "created_at",
        )


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
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
        data["contacts"] = InfoContactSerializer(
            instance.contacts.all(), many=True
        ).data
        return data
