from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

from accounts.models import User
from adopt_assignment.models import AdoptAssignment
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.size
    limit_mb = 3
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("이미지의 최대 크기는 %s MB 입니다." % limit_mb)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Review(TimestampedModel):
    review_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, db_index=True,
                             validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
                             ])
    content = models.TextField()
    image1 = models.ImageField(blank=True, validators=[validate_image])
    image2 = models.ImageField(blank=True, validators=[validate_image])
    image3 = models.ImageField(blank=True, validators=[validate_image])
    image4 = models.ImageField(blank=True, validators=[validate_image])
    image5 = models.ImageField(blank=True, validators=[validate_image])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adoptassignment = models.ForeignKey(AdoptAssignment, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-review_no']

