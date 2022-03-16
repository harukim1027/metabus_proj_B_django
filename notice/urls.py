from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notice.views import NoticeViewSet


app_name = 'notice'

router = DefaultRouter()
router.register("notices", NoticeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

