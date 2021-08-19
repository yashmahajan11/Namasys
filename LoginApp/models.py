from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    address = models.TextField(blank=False)

    class Meta:
        db_table = "CustomUser"