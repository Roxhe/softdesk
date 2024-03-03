from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        if self.birthdate:
            today = timezone.now().date()
            age = today.year - self.birthdate.year - \
                ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            if age < 15:
                raise ValidationError("User must be at least 15 years old")

    def __str__(self):
        return self.username
