
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     ROLE_CHOICES = (
#         ('manager', 'Farm Manager'),
#         ('worker', 'Field Worker'),
#     )
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='worker')
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('worker', 'Worker'),
        ('manager', 'Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='worker')

    def __str__(self):
        return self.username