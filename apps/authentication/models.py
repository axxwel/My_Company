from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'
    
class App_admin(models.Model):
    def __str__(self):
        return f'{self.app_name}'
    app_name = models.fields.CharField(max_length=30, unique=True)
    admin_members = models.ManyToManyField(User)

class Company(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    controler = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='company_controler')
    super_controler = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='company_super_controler')

class Branch(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    controler = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='branch_controler')
    members = models.ManyToManyField(User, blank=True)

""" def populate_data(sender, **kwargs):
    password='Soleil1234'

    # Create a user
    super_admin = User.objects.create_user(username='super_admin', password=password)

    company_super_controler = User.objects.create_user(username='company_super_controler', password=password)
    company_controler = User.objects.create_user(username='company_controler', password=password)

    controler_A = User.objects.create_user(username='controler_A', password=password)
    controler_B = User.objects.create_user(username='controler_B', password=password)

    user_A = User.objects.create_user(username='user_A', password=password)
    user_B = User.objects.create_user(username='user_B', password=password)

    purchases_auth_admin = User.objects.create_user(username='purchases_auth_admin', password=password)

    # Create an app_admin
    purchases_auth = App_admin.objects.create(app_name='purchases_auth')
    purchases_auth.admin_members.add(purchases_auth_admin)

    # Create a company
    company = Company.objects.create(name='Company_A')
    company.controler = company_controler
    company.super_controler = company_super_controler

    # Create a branch
    branch_A = Branch.objects.create(name='Branch A', company=company)
    branch_A.controler = controler_A
    branch_A.members.add(controler_A)
    branch_A.members.add(user_A)

    branch_B = Branch.objects.create(name='Branch B', company=company)
    branch_B.controler = controler_B
    branch_B.members.add(controler_B)
    branch_B.members.add(user_B)

    post_migrate.connect(populate_data, sender='authentication') """