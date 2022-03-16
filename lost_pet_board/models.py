import os

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


# 잃어버렸어요 게시판
class LostPetBoard(TimestampedModel):
    lost_board_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    pet_name = models.CharField(max_length=20)
    breed = models.TextField()
    size = models.CharField(max_length=10)
    lost_location = models.TextField()

    Lost_time = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-lost_board_no']


# 잃어버렸어요 게시판 이미지
class LostPetBoardImage(models.Model):
    lost_image_no = models.AutoField(primary_key=True)

    image1 = models.ImageField(blank=False, validators=[validate_image])
    image2 = models.ImageField(blank=True, validators=[validate_image])
    image3 = models.ImageField(blank=True, validators=[validate_image])

    lost_board_no = models.ForeignKey(LostPetBoard, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-lost_image_no']


# 잃어버렸어요 게시판 댓글
class LostPetBoardComment(TimestampedModel):
    lost_comment_no = models.AutoField(primary_key=True)

    comment_content = models.TextField()

    lost_board_no = models.ForeignKey(LostPetBoard, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-lost_comment_no']
