"""Database settings of the 'Users' app."""
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.user_manager import CustomUserManager
from users.validators import (
    CustomPasswordValidator,
    validate_email_field,
    validate_first_name_and_last_name_fields,
)


class User(AbstractUser):
    username = None
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=settings.MAX_LEN_FULL_NAME_USER_MODEL,
        blank=False,
        validators=[validate_first_name_and_last_name_fields],
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=settings.MAX_LEN_FULL_NAME_USER_MODEL,
        blank=False,
        validators=[validate_first_name_and_last_name_fields],
    )
    email = models.EmailField(
        verbose_name="Почта",
        max_length=settings.MAX_LEN_EMAIL_USER_MODEL,
        blank=False,
        unique=True,
        validators=[validate_email_field],
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        validator = CustomPasswordValidator()
        validator.validate(self.password)
        self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
