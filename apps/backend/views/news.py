from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.news import News, NewsCategory
from apps.backend.serializers.news import (
    NewsSerializer,
    NewsDetailSerializer,
    NewsCategorySerializer,
)
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class NewsList(APIView):
    serializer_class = NewsSerializer

    def get(self, request):
        queryset = News.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class NewsDetail(APIView):
    serializer_class = NewsDetailSerializer

    def get(self, request, pk):
        news = get_object_or_404(News, pk)
        serializer = self.serializer_class(news)
        return Response(
            {
                "success": True,
                "message": "News fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class NewsCategoryList(APIView):
    serializer_class = NewsCategorySerializer

    def get(self, request):
        queryset = NewsCategory.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
