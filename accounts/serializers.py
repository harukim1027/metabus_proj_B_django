from typing import Dict
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework import serializers

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)

from django import forms

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    # nickname: CHAR(20) NOT NULL
    # name: CHAR(30) NOT NULL
    # password: CHAR(20) NOT NULL
    # phone_number: CHAR(16) NOT NULL
    # email: CHAR(50) NOT NULL
    # region: CHAR(20) NOT NULL
    # password_quiz: CHAR(30) NOT NULL
    # password_quiz_answer: CHAR(30) NOT NULL
    # created_at: DATETIME NOT NULL
    # updated_at: DATETIME NOT NULL

    class Meta:
        model = User
        fields = ["userID", "nickname", 'name', "password", "password2", "phone_number", "email", "region",
                  "password_quiz",
                  "password_quiz_answer"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("동일한 비밀번호를 입력해주세요.")
        return attrs

    def create(self, validated_data):
        userID = validated_data["userID"]
        nickname = validated_data["nickname"]
        name = validated_data['name']
        phone_number = validated_data['phone_number']
        password = validated_data["password"]
        email = validated_data['email']
        region = validated_data["region"]
        password_quiz = validated_data['password_quiz']
        password_quiz_answer = validated_data['password_quiz_answer']

        new_user = User(userID=userID, nickname=nickname, name=name, phone_number=phone_number, email=email,
                        region=region, password_quiz=password_quiz,
                        password_quiz_answer=password_quiz_answer)
        new_user.set_password(password)
        new_user.save()

        return new_user


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    def validate(self, attrs):
        data: Dict = super().validate(attrs)
        data["userID"] = self.user.userID
        data["nickname"] = self.user.nickname
        data["name"] = self.user.name
        data["phone_number"] = self.user.phone_number
        data["email"] = self.user.email
        data["region"] = self.user.region
        data["password_quiz"] = self.user.password_quiz
        data["password_quiz_answer"] = self.user.password_quiz_answer
        data["is_staff"] = self.user.is_staff
        return data


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass


# 로그인한 상태에서 마이페이지에서 비밀 번호 수정을 위한 View
class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """

    error_messages = {
        **SetPasswordForm.error_messages,
        "password_incorrect":
            "Your old password was entered incorrectly. Please enter it again."
        ,
    }
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )

    field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password
