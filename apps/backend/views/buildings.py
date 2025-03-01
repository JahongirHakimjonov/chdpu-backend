from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.buildings import Building
from apps.backend.serializers.buildings import (
    BuildingSerializer,
    BuildingDetailSerializer,
)
from apps.shared.exceptions import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class BuildingList(APIView):
    serializer_class = BuildingSerializer

    def get(self, request):
        queryset = Building.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class BuildingDetail(APIView):
    serializer_class = BuildingDetailSerializer

    @extend_schema(
        operation_id="get_building",
    )
    def get(self, request, pk):
        queryset = get_object_or_404(Building, pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Building retrieved successfully",
                "data": serializer.data,
            }
        )
