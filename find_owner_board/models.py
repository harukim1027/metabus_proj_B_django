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


# 주인찾습니다 게시판
class FindOwnerBoard(TimestampedModel):
    find_board_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, db_index=True)
    content = models.TextField()
    animal_type = models.CharField(max_length=10)
    breed = models.CharField(max_length=18)
    size = models.CharField(max_length=10)
    animal_tag = models.CharField(max_length=30)
    find_location = models.CharField(max_length=50)
    find_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-find_board_no']


# 주인찾습니다 게시판 댓글
class FindOwnerBoardComment(TimestampedModel):
    find_comment_no = models.AutoField(primary_key=True)
    comment_content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    find_board_no = models.ForeignKey(FindOwnerBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['find_comment_no']


# 주인찾습니다 이미지
class FindOwnerBoardImage(TimestampedModel):
    find_image_no = models.AutoField(primary_key=True)
    image = models.ImageField(blank=False, null=False, validators=[validate_image])
    find_board_no = models.ForeignKey(FindOwnerBoard, on_delete=models.CASCADE, related_name="board_image")

    class Meta:
        ordering = ['-find_image_no']

