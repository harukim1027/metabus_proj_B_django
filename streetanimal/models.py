from django.db import models
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.size
    limit_mb = 3
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("이미지의 최대 크기는 %s MB 입니다." % limit_mb)


class AllSecurityCenter(models.Model):
    center_name = models.CharField(max_length=30, unique=True, primary_key=True)
    center_call = models.CharField(max_length=14)
    center_address = models.TextField()

    def __str__(self):
        return self.center_name


class Animal(models.Model):
    announce_no = models.CharField(primary_key=True, max_length=60)
    kind_of_animal = models.CharField(max_length=40)
    breed = models.CharField(max_length=40)
    color = models.CharField(max_length=40)

    # choices 필드
    sex = models.CharField(max_length=30)

    age = models.CharField(max_length=40)
    weight = models.CharField(max_length=30)

    place_of_discovery = models.TextField()

    date_time_of_receipt = models.TextField()

    neutering = models.CharField(max_length=30)

    info = models.TextField()
    competent_organization = models.TextField()
    protect_status = models.CharField(max_length=18)

    image_url1 = models.TextField()
    image_url2 = models.TextField(null=True)
    image_url3 = models.TextField(null=True)

    center_name = models.ForeignKey(AllSecurityCenter, on_delete=models.CASCADE)

    def __str__(self):
        return self.announce_no

    class Meta:
        ordering = ['-announce_no']


