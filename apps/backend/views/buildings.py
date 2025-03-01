from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.buildings import Building
from apps.backend.serializers.buildings import (
    BuildingSerializer,
)


class BuildingList(APIView):
    serializer_class = BuildingSerializer

    def get(self, request):
        queryset = Building.objects.last()
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Data fetched successfully",
                "data": serializer.data,
            }
        )
