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


# 입양 다이어리
class Review(TimestampedModel):
    review_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, db_index=True,
                             validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
                             ])
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adoptassignment = models.ForeignKey(AdoptAssignment, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-review_no']


# 입양 다이어리 후기 사진
class AdoptReviewImage(models.Model):
    review_image_no = models.AutoField(primary_key=True)
    image = models.ImageField(null=False, validators=[validate_image])
    review_no = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_image")

    class Meta:
        ordering = ['-review_image_no']


# 입양 다이어리 게시판 댓글
class AdoptReviewComment(TimestampedModel):
    review_comment_no = models.AutoField(primary_key=True)
    comment_content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['review_comment_no']
