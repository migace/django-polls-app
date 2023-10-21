from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email not provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_trainer', True)
        kwargs.setdefault('is_client', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        if kwargs.get('is_active') is not True:
            raise ValueError("Superuser should be active")
        if kwargs.get('is_trainer') is not True:
            raise ValueError("Superuser should be a trainer")
        if kwargs.get('is_client') is not True:
            raise ValueError("Superuser should be a client")
        if kwargs.get('is_superuser') is not True:
            raise ValueError("Superuser should have is_superuser=True")
        if kwargs.get('is_staff') is not True:
            raise ValueError("Superuser should be staff")
        return self.create_user(email, password, **kwargs)


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_trainer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()
