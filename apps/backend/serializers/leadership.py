from rest_framework import serializers

from apps.backend.models.leadership import Leadership, WorkTimeline


class WorkTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTimeline
        fields = (
            "id",
            "day",
            "start_time",
            "end_time",
        )


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = (
            "id",
            "title",
            "sub_title",
            "contact",
            "image",
            "created_at",
        )


class LeadershipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = (
            "id",
            "title",
            "sub_title",
            "description",
            "description_uz",
            "description_ru",
            "description_en",
            "contact",
            "image",
            "created_at",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["workdays"] = WorkTimelineSerializer(
            instance.work_timelines.all(), many=True
        ).data
        return representation
