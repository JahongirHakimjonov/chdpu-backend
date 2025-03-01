from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.rating import Rating
from apps.backend.serializers.rating import RatingSerializer


class RatingList(APIView):
    serializer_class = RatingSerializer

    def get(self, request):
        queryset = Rating.objects.last()
        serializer = self.serializer_class(queryset)
        return Response(
            {
                "success": True,
                "message": "Data fetched successfully",
                "data": serializer.data,
            }
        )
