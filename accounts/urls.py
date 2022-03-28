from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import TokenObtainPairView, TokenRefreshView, SignupAPIView, UserViewSet, UserPageViewSet, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, UserActivate

app_name = "accounts"

router = DefaultRouter()
router.register("usersnotpaging", UserViewSet)
router.register("users", UserPageViewSet)

urlpatterns = [
    path("api/", include(router.urls)),

]

# 이메일 인증을 위한 API 2개
# POST  accounts/signgup : 회원가입 후 인증 메일 전송
# GET accounts/activate : 인증 메일 클릭 시 해당 아이디를 활성화


urlpatterns += [
    # 회원가입 후 인증 메일 전송을 위한 APIVIew
    path("api/signup/", SignupAPIView.as_view(), name="signup"),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_view"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path(
        "password_change/", PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),

    # 인증메일 활성화를 위한 path
    path('activate/<str:uidb64>/<str:token>/', UserActivate.as_view(), name="activate"),]
