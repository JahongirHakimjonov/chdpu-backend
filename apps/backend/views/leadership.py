from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.leadership import Leadership
from apps.backend.serializers.leadership import (
    LeadershipSerializer,
    LeadershipDetailSerializer,
)
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class LeadershipList(APIView):
    serializer_class = LeadershipSerializer

    def get(self, request):
        queryset = Leadership.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class LeadershipDetail(APIView):
    serializer_class = LeadershipDetailSerializer

    @extend_schema(
        operation_id="leadership",
    )
    def get(self, request, pk):
        leadership = get_object_or_404(Leadership, pk)
        serializer = self.serializer_class(leadership)
        return Response(
            {
                "success": True,
                "message": "Leadership fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
