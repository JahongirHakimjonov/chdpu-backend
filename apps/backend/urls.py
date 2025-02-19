from django.urls import path

from apps.backend.views.chair import ChairList, ChairDetail
from apps.backend.views.cooperation import CooperationList, CooperationDetail
from apps.backend.views.info import InfoList, InfoDetail
from apps.backend.views.interview import InterviewList, InterviewDetail
from apps.backend.views.laboratory import LaboratoryList, LaboratoryDetail
from apps.backend.views.leadership import LeadershipList, LeadershipDetail
from apps.backend.views.news import NewsList, NewsDetail
from apps.backend.views.students import StudentList, StudentDetail

urlpatterns = [
    path("chairs/", ChairList.as_view(), name="chairs"),
    path("chairs/<int:pk>/", ChairDetail.as_view(), name="chair_detail"),
    path("cooperations/", CooperationList.as_view(), name="cooperations"),
    path(
        "cooperations/<int:pk>/", CooperationDetail.as_view(), name="cooperation_detail"
    ),
    path("info/", InfoList.as_view(), name="info"),
    path("info/<int:pk>/", InfoDetail.as_view(), name="info_detail"),
    path("interviews/", InterviewList.as_view(), name="interviews"),
    path("interviews/<int:pk>/", InterviewDetail.as_view(), name="interview_detail"),
    path("laboratories/", LaboratoryList.as_view(), name="laboratories"),
    path(
        "laboratories/<int:pk>/", LaboratoryDetail.as_view(), name="laboratory_detail"
    ),
    path("leaderships/", LeadershipList.as_view(), name="leaderships"),
    path("leaderships/<int:pk>/", LeadershipDetail.as_view(), name="leadership_detail"),
    path("news/", NewsList.as_view(), name="news"),
    path("news/<int:pk>/", NewsDetail.as_view(), name="news_detail"),
    path("students/", StudentList.as_view(), name="students"),
    path("students/<int:pk>/", StudentDetail.as_view(), name="student_detail"),
]
