from django.urls import include, path
from rest_framework.routers import DefaultRouter
from lost_pet_board.views import LostPetViewSet

app_name = "lost_pet_board"

router = DefaultRouter()
router.register("posts", LostPetViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
