from django.urls import include, path
from rest_framework.routers import DefaultRouter

from adopt_review.views import ReviewViewSet, CommentViewSet, ReviewAllViewSet, ReviewImageViewSet

app_name = "adopt_review"

router = DefaultRouter()
router.register("reviews", ReviewViewSet)
router.register("comments", CommentViewSet)
router.register("allreviews", ReviewAllViewSet)
router.register("images", ReviewImageViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
