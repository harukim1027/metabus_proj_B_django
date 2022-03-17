from django.db import models
from accounts.models import User



class InfraCategory(models.Model):
    CATEGORY = (
        ("동물병원", "동물병원"),
        ("동물용품 상점", "동물병원 상점"),
        ("반려동물미용", "반려동물미용"),
        ("펫호텔", "펫호텔"),
    )
    category_name = models.CharField(
        choices=CATEGORY, db_index=True, verbose_name="분류", max_length=30, primary_key=True
    )

    def __str__(self):
        return self.category_name


# 주변 인프라
class AroundInfra(models.Model):
    infra_name = models.CharField(max_length=50, primary_key=True)
    infra_address = models.TextField()
    infra_call = models.CharField(max_length=13, null=True)

    category_name = models.ForeignKey(InfraCategory, on_delete=models.CASCADE, verbose_name="분류", default="동물병원")

    class Meta:
        ordering = ['-infra_name']
