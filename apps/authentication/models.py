from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'

class Company(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    controler_login = models.OneToOneField(User,unique=True , on_delete=models.CASCADE, related_name='company_controler')
    super_controler_login = models.OneToOneField(User,unique=True , on_delete=models.CASCADE, related_name='company_super_controler')

    purchases_auth_admin = models.OneToOneField(User,unique=True , on_delete=models.CASCADE, related_name='purchases_auth_admin')

class Branch(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    controler_login = models.OneToOneField(User,unique=True , on_delete=models.CASCADE, related_name='branch_controler')
    members = models.ManyToManyField(User)

