from django.urls import include, path
from rest_framework.routers import DefaultRouter
from find_owner_board.views import FindOwnerBoardViewSet, FindOwnerBoardCommentViewSet, FindOwnerBoardImageViewSet

app_name = "find_owner_board"

router = DefaultRouter()
router.register("posts", FindOwnerBoardViewSet)
# router.register("find_owner_board", FindOwnerBoardCommentViewSet)
# router.register("find_owner_board", FindOwnerBoardImageViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
