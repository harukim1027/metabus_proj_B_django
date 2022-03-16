from django.db import models
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


class All_security_center(models.Model):
    center_name = models.CharField(max_length=30, unique=True, primary_key=True)
    center_address = models.TextField()
    center_call = models.CharField(max_length=14)

    def __str__(self):
        return self.center_name


class Animal(TimestampedModel):
    announce_no = models.CharField(max_length=30, unique=True, primary_key=True)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=(
        ("암컷", "암컷"),
        ("수컷", "수컷"),
    ), default="암컷")
    age = models.IntegerField()
    weight = models.IntegerField()
    find_location = models.CharField(max_length=50)
    find_time = models.DateField()
    neutering = models.BooleanField()
    info = models.TextField()
    status = models.CharField(max_length=30)
    center_name = models.ForeignKey(All_security_center, on_delete=models.CASCADE)

    def __str__(self):
        return self.announce_no

    class Meta:
        ordering = ['announce_no']


class Animal_image(models.Model):
    animal_image_no = models.IntegerField(unique=True, primary_key=True)
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    announce_no = models.ForeignKey(Animal, on_delete=models.CASCADE)

