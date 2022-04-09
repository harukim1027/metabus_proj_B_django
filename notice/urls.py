from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notice.views import NoticeViewSet, NoticeImageViewSet, NoticeFileViewSet

app_name = 'notice'

router = DefaultRouter()
router.register("notices", NoticeViewSet)
router.register("images", NoticeImageViewSet)
router.register("files", NoticeFileViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

