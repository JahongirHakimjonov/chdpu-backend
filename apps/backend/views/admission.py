from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.admission import Admission
from apps.backend.serializers.admission import (
    AdmissionSerializer,
)


class AdmissionList(APIView):
    serializer_class = AdmissionSerializer

    def get(self, request):
        queryset = Admission.objects.last()
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Admission list retrieved successfully",
                "data": serializer.data,
            }
        )
