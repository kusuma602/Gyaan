from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    profile_pic = models.URLField(default="https//image.jpeg")
    is_admin = models.BooleanField(default=False)
    is_domain_expert = models.BooleanField(default=False)
