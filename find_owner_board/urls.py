from django.urls import include, path
from rest_framework.routers import DefaultRouter
from find_owner_board.views import FindOwnerBoardViewSet, FindOwnerBoardImageViewSet

app_name = "find_owner_board"

router = DefaultRouter()
router.register("board", FindOwnerBoardViewSet)
router.register("images", FindOwnerBoardImageViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
