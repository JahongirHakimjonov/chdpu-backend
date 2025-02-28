from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.backend.models.students import Student
from apps.backend.serializers.students import StudentSerializer, StudentDetailSerializer
from apps.shared.exceptions.http404 import get_object_or_404
from apps.shared.pagination.custom import CustomPagination


class StudentList(APIView):
    serializer_class = StudentSerializer

    def get(self, request):
        queryset = Student.objects.all()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class StudentDetail(APIView):
    serializer_class = StudentDetailSerializer

    def get(self, request, pk):
        student = get_object_or_404(Student, pk)
        serializer = self.serializer_class(student)
        return Response(
            {
                "success": True,
                "message": "Student fetched successfully",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
