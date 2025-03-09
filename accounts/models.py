from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User For Auth: You Can Add Custom Fields
class CustomUser(AbstractUser):
    job = models.CharField(max_length=300)
