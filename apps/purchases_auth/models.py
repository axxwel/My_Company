from datetime import datetime
from django.db import models
from authentification.models import User

class Payment_method(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)

class Purchase_type(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)

class Branch(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    controler_login = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Process(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    Branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    controler_login = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Threshold(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.fields.CharField(max_length=30, unique=True)
    threshold_1 = models.fields.IntegerField()
    threshold_2 = models.fields.IntegerField()
    threshold_3 = models.fields.IntegerField()

    controler = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #super_controler = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Order(models.Model):
    def __str__(self):
        return f'{self.order_id}'

    class auth_status(models.TextChoices):
        AUTHORIZED = 'Authorized'
        REFUSED = 'Refused'
        PENDING = 'Pending'

    order_id = models.fields.CharField(max_length=17, unique=True)
    date = models.fields.DateTimeField(auto_now=True)

    asker_login = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    purchase_type = models.ForeignKey(Purchase_type, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    process = models.ForeignKey(Process, null=True, on_delete=models.SET_NULL)

    payment_method = models.ForeignKey(Payment_method, null=True, on_delete=models.SET_NULL)

    product = models.fields.CharField(max_length=17, unique=True)
    price = models.fields.IntegerField()

    asker_comment = models.fields.CharField(max_length=254, null=True)

    vendor = models.fields.CharField(max_length=17, unique=True)
    unit_price = models.fields.IntegerField()
    delivery_date = models.fields.DateTimeField()

    #controler_login = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    controler_auth = models.fields.CharField(choices=auth_status.choices, default=auth_status.PENDING, max_length=10)
    controler_comment = models.fields.CharField(max_length=254, null=True)
