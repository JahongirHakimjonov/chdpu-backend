from rest_framework import serializers

from apps.backend.models.testimonial import Testimonial
from apps.backend.serializers.chair import ChairSerializer


class TestimonialSerializer(serializers.ModelSerializer):
    chair = ChairSerializer()

    class Meta:
        model = Testimonial
        fields = (
            "id",
            "chair",
            "name",
            "content",
            "image",
            "created_at",
        )
