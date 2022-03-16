from django.urls import include, path
from rest_framework.routers import DefaultRouter
from inquiry_board.views import InquiryViewSet

app_name = "inquiry_board"

router = DefaultRouter()
router.register("inquiry", InquiryViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
