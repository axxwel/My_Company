from django.db import models
from django.conf import settings

from authentication.models import User, Branch, Process

class purchases_auth_admin_goup(models.Model):
    def __str__(self):
        return f'{self.name}'
    members = models.ManyToManyField(User)

class Payment_method(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)

class Purchase_type(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)

class Company_threshold(models.Model):
    def __str__(self):
        return f'{self.name}'
    company = models.fields.CharField(max_length=30, unique=True)
    company_threshold = models.fields.IntegerField(default=6000)
    branch_threshold = models.fields.IntegerField(default=1000)
    process_threshold = models.fields.IntegerField(default=500)

class branch_threshold(models.Model):
    def __str__(self):
        return f'{self.branch}'
    company = models.fields.CharField(max_length=30)
    branch = models.fields.CharField(max_length=30)
    threshold = models.fields.IntegerField(default=Company_threshold.branch_threshold)

class process_threshold(models.Model):
    def __str__(self):
        return f'{self.name}'
    company = models.fields.CharField(max_length=30)
    branch = models.fields.CharField(max_length=30)
    process = models.fields.CharField(max_length=30)
    threshold = models.fields.IntegerField(default=Company_threshold.process_threshold)

class Order(models.Model):
    def __str__(self):
        return f'{self.order_id}'

    class auth_status(models.TextChoices):
        AUTHORIZED = 'Authorized'
        REFUSED = 'Refused'
        PENDING = 'Pending'

    order_id = models.fields.CharField(max_length=17, unique=True)
    date = models.fields.DateTimeField(auto_now=True)

    asker_login = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    purchase_type = models.ForeignKey(Purchase_type, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE)

    product = models.fields.CharField(max_length=17)
    price = models.fields.IntegerField()

    asker_comment = models.fields.CharField(max_length=254, null=True)

    vendor = models.fields.CharField(max_length=17)
    unit_price = models.fields.IntegerField(null=True)
    delivery_date = models.fields.DateField(null=True)

    controler_login = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='order_controler')

    controler_auth = models.fields.CharField(choices=auth_status.choices, default=auth_status.PENDING, max_length=10)
    controler_comment = models.fields.CharField(max_length=254, null=True)