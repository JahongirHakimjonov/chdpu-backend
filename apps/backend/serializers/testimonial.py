from rest_framework import serializers

from apps.backend.models.testimonial import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
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
