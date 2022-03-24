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


class AllSecurityCenter(models.Model):
    center_name = models.CharField(max_length=30, unique=True, primary_key=True)
    center_address = models.TextField()
    center_call = models.CharField(max_length=14)

    def __str__(self):
        return self.center_name


class Animal(TimestampedModel):
    announce_no = models.CharField(primary_key=True, max_length=30)
    kind_of_animal = models.CharField(max_length=18)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    neutering = models.CharField(max_length=10)
    info = models.TextField()
    date_time_of_receipt = models.DateTimeField()
    reason_for_rescue=models.TextField()
    place_of_discovery = models.CharField(max_length=50)
    period_of_announcement = models.DateField()
    shelter = models.CharField(max_length=30)
    center_call = models.CharField(max_length=18, default=False)
    person_in_charge = models.CharField(max_length=18, default=False)
    significant = models.TextField(default=False)
    
    center_name = models.ForeignKey(AllSecurityCenter, on_delete=models.CASCADE)

    def __str__(self):
        return self.announce_no

    class Meta:
        ordering = ['-announce_no']


# 유기동물 이미지
class AnimalImage(models.Model):
    animal_image_no = models.AutoField(primary_key=True)

    image = models.ImageField(blank=False, validators=[validate_image])

    announce_no = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="announce_image")

    class Meta:
        ordering = ['-animal_image_no']