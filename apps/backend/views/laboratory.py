from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.laboratory import Laboratory
from apps.backend.serializers.laboratory import (
    LaboratorySerializer,
    LaboratoryDetailSerializer,
)
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class LaboratoryList(APIView):
    serializer_class = LaboratorySerializer

    def get(self, request):
        queryset = Laboratory.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class LaboratoryDetail(APIView):
    serializer_class = LaboratoryDetailSerializer

    def get(self, request, pk):
        laboratory = get_object_or_404(Laboratory, pk)
        serializer = self.serializer_class(laboratory)
        return Response(
            {
                "success": True,
                "message": "Laboratory fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
