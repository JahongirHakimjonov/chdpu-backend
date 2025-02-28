from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.chair import Chair, ChairMember
from apps.backend.serializers.chair import (
    ChairSerializer,
    ChairMemberSerializer,
    ChairDetailSerializer,
    ChairMemberDetailSerializer,
)
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
    serializer_class = ChairDetailSerializer

    @extend_schema(
        operation_id="chairs-retrieve",
    )
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


class ChairMemberList(APIView):
    serializer_class = ChairMemberSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="chair",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Chair ID",
            )
        ]
    )
    def get(self, request):
        queryset = ChairMember.objects.all()
        chair = request.query_params.get("chair", None)
        if chair:
            queryset = queryset.filter(chair=chair)
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ChairMemberDetail(APIView):
    serializer_class = ChairMemberDetailSerializer

    @extend_schema(
        operation_id="chairs-member-retrieve",
    )
    def get(self, request, pk):
        chair_member = get_object_or_404(ChairMember, pk)
        serializer = self.serializer_class(chair_member)
        return Response(
            {
                "success": True,
                "message": "Chair Member fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
