from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.chair import Chair
from apps.backend.serializers.chair import ChairSerializer
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class ChairList(APIView):
    serializer_class = ChairSerializer

    def get(self, request):
        queryset = Chair.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ChairDetail(APIView):
    serializer_class = ChairSerializer

    def get(self, request, pk):
        chair = get_object_or_404(Chair, pk)
        serializer = self.serializer_class(chair)
        return Response(
            {
                "success": True,
                "message": "Chair fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
