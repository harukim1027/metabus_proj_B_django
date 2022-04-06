from django.urls import include, path
from rest_framework.routers import DefaultRouter
from find_owner_board.views import FindOwnerBoardViewSet, FindOwnerBoardImageViewSet, CommentViewSet

app_name = "find_owner_board"

router = DefaultRouter()
router.register("board", FindOwnerBoardViewSet)
router.register("images", FindOwnerBoardImageViewSet)
router.register("comments", CommentViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
