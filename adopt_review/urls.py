from django.urls import include, path
from rest_framework.routers import DefaultRouter

from adopt_review import views
from adopt_review.views import ReviewViewSet, CommentViewset

app_name = "adopt_review"

router = DefaultRouter()
router.register("reviews", ReviewViewSet)
router.register("comments", CommentViewset)


urlpatterns = [
    path("api/", include(router.urls)),
]
