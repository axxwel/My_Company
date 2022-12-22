from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE,)
    process = models.ForeignKey('Process', on_delete=models.CASCADE)

class Branch(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    controler_login = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, on_delete=models.CASCADE)

class Process(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    Branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    controler_login = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, on_delete=models.CASCADE)