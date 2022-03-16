from django.urls import path, include
from rest_framework.routers import DefaultRouter
from streetanimal.views import AnimalViewSet, AnimalPageViewSet

app_name = 'streetanimal'

router = DefaultRouter()
router.register("animalnotpaging", AnimalViewSet)
router.register("animal", AnimalPageViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

