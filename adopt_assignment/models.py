from django.conf import settings
from django.db import models

from accounts.models import User
from streetanimal.models import Animal
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.size
    limit_mb = 3
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("이미지의 최대 크기는 %s MB 입니다." % limit_mb)


class TimestampedModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class AdoptAssignment(TimestampedModel):
    assignment_no = models.AutoField(primary_key=True)
    adopter_name = models.CharField(max_length=30, db_index=True)
    monthly_income = models.IntegerField()
    residential_type = models.CharField(max_length=50, choices=[
        ("아파트", "아파트"),
        ("빌라", "빌라"),
        ("주택", "주택"),
        ("원룸", "원룸"),
        ("오피스텔", "오피스텔"),
    ], default="아파트")
    have_pet_or_not = models.BooleanField()
    date_to_meet = models.DateField()
    status = models.CharField(max_length=30, choices=(
        ("신청", "신청"),
        ("심사 중", "심사 중"),
        ("수락", "수락"),
        ("교육 중", "교육 중"),
        ("입양 완료", "입양 완료"),
        ("거절", "거절"),
    ), default="신청", db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, unique=True)



    class Meta:
        ordering = ['-assignment_no']


# 입양 신청 거주지 사진
class AdoptAssignmentHomeImage(models.Model):
    home_image_no = models.AutoField(primary_key=True)
    image = models.ImageField(validators=[validate_image])
    assignment_no = models.ForeignKey(AdoptAssignment, on_delete=models.CASCADE, related_name="home_image")

    class Meta:
        ordering = ['-home_image_no']

