import os
from uuid import uuid4

from django.conf import settings
from django.db import models

from accounts.models import User
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


class Notice(TimestampedModel):
    notice_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-notice_no']


# 공지사항 이미지
class NoticeImage(models.Model):
    notice_image_no = models.AutoField(primary_key=True)

    image = models.ImageField(blank=True, validators=[validate_image])

    notice_no = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name="notice_image")

    class Meta:
        ordering = ['-notice_image_no']


# 공지사항 첨부파일
class NoticeFile(models.Model):
    notice_file_no = models.AutoField(primary_key=True)

    file = models.FileField(blank=True)
    filename = models.CharField(max_length=100)

    notice_no = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name="notice_file")

    class Meta:
        ordering = ['-notice_file_no']

    def get_file_name1(self):
        return os.path.basename(self.file.name)