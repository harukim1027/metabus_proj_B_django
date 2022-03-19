import traceback
import bcrypt
import requests



from django.conf import settings
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordContextMixin
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, TemplateView
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OriginTokenObtainPairView,
    TokenRefreshView as OriginTokenRefreshView,
)

from accounts.serializers import TokenObtainPairSerializer, UserCreationSerializer, UserSerializer
from notice.paginations.Pagination import Pagination

from django.contrib.auth import login as auth_login

from rest_framework import mixins

# 이메일 인증을 위한 import 추가
from django.contrib.auth.mixins import UserPassesTestMixin
import json
from .models import User
from .tokens import account_activation_token
from .text import message

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

# email 전송을 위한 import 추가
from django.core.mail.message import EmailMessage

User = get_user_model()


class UserPageViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Pagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(userID__icontains=query) or qs.filter(nickname__icontains=query) or qs.filter(
                name__icontains=query)

        return qs


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(userID__icontains=query) or qs.filter(name__icontains=query) or qs.filter(
                nickname__icontains=query)

        return qs


# 회원 가입 및 이메일 전송을 위한 API View  : 회원가입에 성공하면 인증 이메일을 전송
#
# 기존 것

class CreateAPIView(mixins.CreateModelMixin, GenericAPIView):

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)


class SignupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]



class TokenObtainPairView(OriginTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OriginTokenRefreshView):
    pass


# # 메시지 전송 테스트
# def send_email(request):
#     subject = "message"
#     to = ["metabusemail@gmail.com"]
#     from_email = "metabusemail@gmail.com"
#     message = "메시지 테스트"
#     EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()


#  password 변경을 위한 view 들
# 기본 auth 뷰를 사용하지 않고, views.py에 기존 형식은 그대로 두되,
# success_url = reverse_lazy("accounts:password_reset_done") 부분에 app_name 인 accounts 를 추가

# 추가
UserModel = get_user_model()


class SuccessURLAllowedHostsMixin:
    success_url_allowed_hosts = set()

    def __init__(self):
        self.request = None

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}


class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {"title": self.title, "subtitle": None, **(self.extra_context or {})}
        )
        return context


# 비밀번호 리셋을 위해 이메일을 입력하는 폼 view
class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = "registration/password_reset_email.html"
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy("accounts:password_reset_done")
    template_name = "registration/password_reset_form.html"
    title = "Password reset"
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)


INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"


# 비밀번호 변경 이메일을 보낸 후의 완료 메시지 띄우는 view
class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_reset_done.html"
    title = "Password reset sent"


# 해당 이메일로 링크를 보낸 후, 링크에 접속하면 뜨는
# 비밀번호 변경을 위한 form view
class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = "set-password"
    success_url = reverse_lazy("accounts:password_reset_complete")
    template_name = "registration/password_reset_confirm.html"
    title = "Enter new password"
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if "uidb64" not in kwargs or "token" not in kwargs:
            raise ImproperlyConfigured(
                "The URL path must contain 'uidb64' and 'token' parameters."
            )

        self.validlink = False
        self.user = self.get_user(kwargs["uidb64"])

        if self.user is not None:
            token = kwargs["token"]
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(
                        token, self.reset_url_token
                    )
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                UserModel.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context["validlink"] = True
        else:
            context.update(
                {
                    "form": None,
                    "title": "Password reset unsuccessful",
                    "validlink": False,
                }
            )
        return context


class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_reset_complete.html"
    title = "Password reset complete"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context


class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("accounts:password_change_done")
    template_name = "registration/password_change_form.html"
    title = "Password change"

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_change_done.html"
    title = "Password change successful"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# 이메일 인증을 위한 view


class UserActivate(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        try:
            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return Response(user.email + '계정이 활성화 되었습니다.', status=status.HTTP_200_OK)
            else:
                return Response("만료된 링크입니다.", status=status.HTTP_400_BAD_REQUEST)


        except Exception:
            print(traceback.format_exc())
