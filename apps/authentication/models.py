from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_controler = models.fields.BooleanField(default = False)

