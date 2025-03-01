from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.rating import Rating
from apps.backend.serializers.rating import RatingSerializer, RatingDetailSerializer
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class RatingList(APIView):
    serializer_class = RatingSerializer

    def get(self, request):
        queryset = Rating.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class RatingDetail(APIView):
    serializer_class = RatingDetailSerializer

    @extend_schema(
        operation_id="get_rating",
    )
    def get(self, request, pk):
        queryset = get_object_or_404(Rating, pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Rating retrieved successfully",
                "data": serializer.data,
            }
        )
