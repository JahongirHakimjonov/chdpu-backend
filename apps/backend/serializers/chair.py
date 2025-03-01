from rest_framework import serializers

from apps.backend.models.chair import Chair, ChairMember, ChairContact


class ChairContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChairContact
        fields = (
            "id",
            "chair",
            "contact_type",
            "value",
            "created_at",
        )


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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["members"] = ChairMemberDetailSerializer(
            instance.members.all(), many=True
        ).data
        data["contacts"] = ChairContactSerializer(
            instance.contacts.all(), many=True
        ).data
        return data
