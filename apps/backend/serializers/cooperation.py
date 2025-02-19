from rest_framework import serializers

from apps.backend.models.cooperation import Cooperation


class CooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperation
        fields = "__all__"
