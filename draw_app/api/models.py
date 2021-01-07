from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Competitor(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=64)
    verified = models.BooleanField(default=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
