from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    # Thêm 2 dòng này vào nếu thiếu:
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username