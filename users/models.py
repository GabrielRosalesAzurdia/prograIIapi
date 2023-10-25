from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    rol = models.IntegerField( default=0)
    phone = models.TextField( default="")
    adress = models.TextField( default="")
    employeeNumber = models.TextField(default="")
    schedule = models.IntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["rol","phone","adress","employeeNumber","schedule"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email