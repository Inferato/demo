from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    pass

class MyCustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10, unique=True, help_text="Enter your phone number")
    profile_image = models.ImageField(upload_to="media")

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


