from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    # Đề bài yêu cầu: id, name, email, password
    # AbstractUser đã có sẵn: id, username, password, email.
    # Ta thêm trường 'name' như đề bài yêu cầu [cite: 240]
    name = models.CharField(max_length=255, default="")
    
    # Các dòng dưới đây để tránh xung đột với user mặc định của Django
    groups = models.ManyToManyField(
        'auth.Group', related_name='customer_groups', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='customer_permissions', blank=True
    )

    def __str__(self):
        return self.username