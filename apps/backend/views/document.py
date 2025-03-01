from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.document import Document
from apps.backend.serializers.document import (
    DocumentSerializer,
)


class DocumentList(APIView):
    serializer_class = DocumentSerializer

    def get(self, request):
        queryset = Document.objects.last()
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Data fetched successfully",
                "data": serializer.data,
            }
        )
