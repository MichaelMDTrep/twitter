from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)


class Tweet(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
