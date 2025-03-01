from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.admission import Admission
from apps.backend.serializers.admission import (
    AdmissionSerializer,
    AdmissionDetailSerializer,
)
from apps.shared.exceptions import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class AdmissionList(APIView):
    serializer_class = AdmissionSerializer

    def get(self, request):
        queryset = Admission.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class AdmissionDetail(APIView):
    serializer_class = AdmissionDetailSerializer

    @extend_schema(
        operation_id="get_admission",
    )
    def get(self, request, pk):
        queryset = get_object_or_404(Admission, pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Admission retrieved successfully",
                "data": serializer.data,
            }
        )
