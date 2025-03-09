from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User For Auth: You Can Add Custom Fields
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('M', 'Manager'),
        ('E', 'Employee'),
        ('S', 'Student'),
        ('O', 'Other'),
    ]
    role = models.CharField(choices=ROLE_CHOICES, max_length=1, default=ROLE_CHOICES[3][0])
