from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.cooperation import Cooperation
from apps.backend.serializers.cooperation import (
    CooperationSerializer,
    CooperationDetailSerializer,
)
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class CooperationList(APIView):
    serializer_class = CooperationSerializer

    def get(self, request):
        queryset = Cooperation.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class CooperationDetail(APIView):
    serializer_class = CooperationDetailSerializer

    def get(self, request, pk):
        cooperation = get_object_or_404(Cooperation, pk)
        serializer = self.serializer_class(cooperation)
        return Response(
            {
                "success": True,
                "message": "Cooperation fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
