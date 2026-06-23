from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    REQUIRED_FIELDS = ["age"]

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(15)],
    )
    can_be_contacted = models.BooleanField(
        default=False,
    )
    can_data_be_shared = models.BooleanField(
        default=False,
    )
