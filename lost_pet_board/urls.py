from django.urls import include, path
from rest_framework.routers import DefaultRouter
from lost_pet_board.views import LostPetViewSet, LostPetBoardImageViewSet, CommentViewSet

app_name = "lost_pet_board"

router = DefaultRouter()
router.register("board", LostPetViewSet)
router.register("images", LostPetBoardImageViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
