from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    dob=models.IntegerField(null=True)

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
