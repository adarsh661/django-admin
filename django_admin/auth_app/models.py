from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    pincode = models.CharField(max_length=6, null=True, blank=True)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)