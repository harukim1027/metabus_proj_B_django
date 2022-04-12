from django.urls import path, include
from rest_framework.routers import DefaultRouter
from streetanimal.views import AnimalViewSet, AnimalPageViewSet, CentersViewSet, stat

app_name = 'streetanimal'

router = DefaultRouter()
router.register("animalnotpaging", AnimalViewSet)
router.register("animal", AnimalPageViewSet)
router.register("centers", CentersViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("stat/", stat),
]

