from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.testimonial import Testimonial
from apps.backend.serializers.testimonial import TestimonialSerializer
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class TestimonialListAPIView(APIView):
    serializer_class = TestimonialSerializer

    def get(self, request):
        testimonials = Testimonial.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(testimonials, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class TestimonialDetailAPIView(APIView):
    serializer_class = TestimonialSerializer

    def get(self, request, pk):
        testimonial = get_object_or_404(Testimonial, pk=pk)
        serializer = self.serializer_class(testimonial)
        return Response(
            {
                "success": True,
                "message": "Testimonial fetched successfully",
                "data": serializer.data,
            }
        )
