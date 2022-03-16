from django.conf import settings
from django.db import models

from accounts.models import User


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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


class FindOwnerBoardComment(TimestampedModel):
    find_comment_no = models.AutoField(primary_key=True)
    comment_content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    find_board_no = models.ForeignKey(FindOwnerBoard, on_delete=models.CASCADE)


class FindOwnerBoardImage(TimestampedModel):
    find_image_no = models.AutoField(primary_key=True)
    image1 = models.TextField()
    image2 = models.TextField(blank=True)
    image3 = models.TextField(blank=True)
    find_board_no = models.ForeignKey(FindOwnerBoard, on_delete=models.CASCADE)


