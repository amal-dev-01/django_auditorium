
from django.contrib.auth.models import AbstractUser
from django.db import models

class Auditorium_Info(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone =models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return self.email










