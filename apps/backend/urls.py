from django.urls import path

from apps.backend.views.admission import AdmissionList
from apps.backend.views.buildings import BuildingList
from apps.backend.views.chair import (
    ChairList,
    ChairDetail,
    ChairMemberList,
    ChairMemberDetail,
)
from apps.backend.views.cooperation import CooperationList, CooperationDetail
from apps.backend.views.document import DocumentList
from apps.backend.views.info import InfoList
from apps.backend.views.interview import InterviewList, InterviewDetail
from apps.backend.views.laboratory import LaboratoryList, LaboratoryDetail
from apps.backend.views.leadership import LeadershipList, LeadershipDetail
from apps.backend.views.news import NewsList, NewsDetail, NewsCategoryList
from apps.backend.views.rating import RatingList
from apps.backend.views.students import StudentList, StudentDetail
from apps.backend.views.testimonial import (
    TestimonialListAPIView,
    TestimonialDetailAPIView,
)

urlpatterns = [
    path("chairs/", ChairList.as_view(), name="chairs"),
    path("chairs/<int:pk>/", ChairDetail.as_view(), name="chair_detail"),
    path("chairs/members/", ChairMemberList.as_view(), name="chairs-members"),
    path(
        "chairs/members/<int:pk>/",
        ChairMemberDetail.as_view(),
        name="chair-member_detail",
    ),
    path("cooperations/", CooperationList.as_view(), name="cooperation"),
    path(
        "cooperations/<int:pk>/", CooperationDetail.as_view(), name="cooperation_detail"
    ),
    path("info/", InfoList.as_view(), name="info"),
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
    path("news/category/", NewsCategoryList.as_view(), name="news-categories"),
    path("students/", StudentList.as_view(), name="students"),
    path("students/<int:pk>/", StudentDetail.as_view(), name="student_detail"),
    path("testimonials/", TestimonialListAPIView.as_view(), name="testimonials"),
    path(
        "testimonials/<int:pk>/",
        TestimonialDetailAPIView.as_view(),
        name="testimonials-detail",
    ),
    path("building/", BuildingList.as_view(), name="building"),
    path("document/", DocumentList.as_view(), name="document"),
    path("rating/", RatingList.as_view(), name="rating"),
    path("admission/", AdmissionList.as_view(), name="admission"),
]
