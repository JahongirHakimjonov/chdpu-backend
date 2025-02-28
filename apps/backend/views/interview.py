from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.interview import Interview
from apps.backend.serializers.interview import (
    InterviewSerializer,
    InterviewDetailSerializer,
)
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class InterviewList(APIView):
    serializer_class = InterviewSerializer

    def get(self, request):
        queryset = Interview.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class InterviewDetail(APIView):
    serializer_class = InterviewDetailSerializer

    def get(self, request, pk):
        interview = get_object_or_404(Interview, pk)
        serializer = self.serializer_class(interview)
        return Response(
            {
                "success": True,
                "message": "Interview fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
