from django.db import models
from django.conf import settings

from authentication.models import User, Company, Branch

class Payment_method(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)

class Purchase_type(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)

class Process(models.Model):
    def __str__(self):
        return f'{self.name}'
    
    name = models.fields.CharField(max_length=30, unique=True)

    purchase_type = models.ForeignKey(Purchase_type, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    company_threshold = models.fields.IntegerField(default=6000)
    branch_threshold = models.fields.IntegerField(default=1000)
    process_threshold = models.fields.IntegerField(default=500)
    controler = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='process_controler')

class Order(models.Model):
    def __str__(self):
        return f'{self.order_id}'

    class auth_status(models.TextChoices):
        AUTHORIZED = 'Authorized'
        REFUSED = 'Refused'
        PENDING = 'Pending'

    order_id = models.fields.CharField(max_length=17, unique=True)
    date = models.fields.DateField(auto_now=True)

    asker_login = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    purchase_type = models.ForeignKey(Purchase_type, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE)

    product = models.fields.CharField(max_length=17)
    price = models.fields.IntegerField()

    asker_comment = models.fields.TextField(max_length = 100, blank=True)

    vendor = models.fields.CharField(max_length=17)
    unit_price = models.fields.IntegerField(blank=True)
    delivery_date = models.fields.DateField()

    controler_login = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='order_controler')

    controler_auth = models.fields.CharField(choices=auth_status.choices, default=auth_status.PENDING, max_length=10)
    controler_comment = models.fields.TextField(max_length = 100, blank=True)