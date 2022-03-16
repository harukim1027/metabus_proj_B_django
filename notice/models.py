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


class Notice(TimestampedModel):
    notice_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image1 = models.ImageField(blank=True, validators=[validate_image])
    image2 = models.ImageField(blank=True, validators=[validate_image])
    image3 = models.ImageField(blank=True, validators=[validate_image])
    image4 = models.ImageField(blank=True, validators=[validate_image])
    image5 = models.ImageField(blank=True, validators=[validate_image])
    file1 = models.FileField(blank=True)
    file2 = models.FileField(blank=True)
    file3 = models.FileField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-notice_no']

    def get_file_name1(self):
        return os.path.basename(self.file1.name)

    def get_file_name2(self):
        return os.path.basename(self.file2.name)

    def get_file_name3(self):
        return os.path.basename(self.file3.name)

    # def get_file_ext(self):
    #     return self.get_file_name().split('.')[-1]

