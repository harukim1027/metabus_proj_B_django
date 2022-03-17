from django.urls import include, path
from rest_framework.routers import DefaultRouter
from around_infra.views import AroundInfraViewSet

app_name = "around_infra"

router = DefaultRouter()
router.register("infra", AroundInfraViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
