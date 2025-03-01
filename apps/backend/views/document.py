from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.document import Document
from apps.backend.serializers.document import (
    DocumentSerializer,
    DocumentDetailSerializer,
)
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class DocumentList(APIView):
    serializer_class = DocumentSerializer

    def get(self, request):
        queryset = Document.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class DocumentDetail(APIView):
    serializer_class = DocumentDetailSerializer

    @extend_schema(
        operation_id="get_document",
    )
    def get(self, request, pk):
        queryset = get_object_or_404(Document, pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Document retrieved successfully",
                "data": serializer.data,
            }
        )
