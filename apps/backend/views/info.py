from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.info import Info
from apps.backend.serializers.info import InfoSerializer


class InfoList(APIView):
    serializer_class = InfoSerializer

    def get(self, request):
        queryset = Info.objects.last()
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Ma'lumotlar",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
