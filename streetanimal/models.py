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


class Category(models.Model):
    CATEGORY = (
        ("강아지", "강아지"),
        ("고양이", "고양이"),
    )
    name = models.CharField(
        choices=CATEGORY, db_index=True, verbose_name="품종", max_length=30, primary_key=True
    )

    def __str__(self):
        return self.name


class Animal(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="동물 종", default="강아지")
    animal_no = models.AutoField(primary_key=True)
    animal_reg_num = models.CharField(max_length=50, unique=True)
    size = models.CharField(max_length=30, choices=(
        ("소형", "소형"),
        ("중형", "중형"),
        ("대형", "대형"),
    ), default="소형")
    sex = models.CharField(max_length=30, choices=(
        ("암컷", "암컷"),
        ("수컷", "수컷"),
    ), default="암컷")
    age = models.IntegerField()
    date_of_discovery = models.DateTimeField()
    place_of_discovery = models.CharField(max_length=30)
    info = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    protection_status = models.CharField(max_length=50, choices=(
        ("입양 대기", "입양 대기"),
        ("입양 매칭 중", "입양 매칭 중"),
        ("입양 완료!", "입양 완료!"),
    ), default="입양 대기")
    image = models.ImageField(blank=True, validators=[validate_image])

    def __str__(self):
        return self.animal_reg_num

    class Meta:
        ordering = ['-animal_no']
