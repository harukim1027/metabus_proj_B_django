from django.urls import path, include
from rest_framework.routers import DefaultRouter

from adopt_assignment.views import AssignmentViewSet, AssignmentPagingViewSet

app_name = "adopt_assignment"

router = DefaultRouter()
router.register("assignment", AssignmentPagingViewSet)
router.register("assignmentnotpaging", AssignmentViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
