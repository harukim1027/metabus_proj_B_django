from django.urls import include, path
from rest_framework.routers import DefaultRouter
from find_owner_board.views import FindOwnerBoardViewSet

app_name = "find_owner_board"

router = DefaultRouter()
router.register("board", FindOwnerBoardViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
