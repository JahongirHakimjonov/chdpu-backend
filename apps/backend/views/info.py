from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.info import Info
from apps.backend.serializers.info import InfoSerializer, InfoDetailSerializer
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class InfoList(APIView):
    serializer_class = InfoSerializer

    def get(self, request):
        queryset = Info.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class InfoDetail(APIView):
    serializer_class = InfoDetailSerializer

    def get(self, request, pk):
        info = get_object_or_404(Info, pk)
        serializer = self.serializer_class(info)
        return Response(
            {
                "success": True,
                "message": "Info fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
