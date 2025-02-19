from rest_framework import serializers

from apps.backend.models.interview import Interview


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"
