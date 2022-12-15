from django.db import models

class Datas(models.Model):
    name = models.fields.CharField(max_length=100)

class User(models.Model):
    name = models.fields.CharField(max_length=100)