from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    sex = models.BooleanField(default=False)