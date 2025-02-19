from rest_framework import serializers

from apps.backend.models.chair import Chair


class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = "__all__"
