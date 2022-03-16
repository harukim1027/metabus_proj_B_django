from django.conf import settings
from django.db import models

from accounts.models import User


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Inquiry(TimestampedModel):
    inquiry_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, db_index=True)
    content = models.TextField()
    admin_answer = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-inquiry_no']
