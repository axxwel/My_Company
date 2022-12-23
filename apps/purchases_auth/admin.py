from django.contrib import admin

from purchases_auth.models import Payment_method
from purchases_auth.models import Purchase_type
from purchases_auth.models import Threshold
from purchases_auth.models import Order
    
class Payment_method_admin(admin.ModelAdmin):
    list_display = ('name',)

class Purchase_type_admin(admin.ModelAdmin):
    list_display = ('name',)

class Branch_admin(admin.ModelAdmin):
    list_display = ('name',)

class Process_admin(admin.ModelAdmin):
    list_display = ('name', 'Branch')


class Threshold_admin(admin.ModelAdmin):
    list_display = ('name', 'threshold_1', 'threshold_2', 'threshold_3')

class Order_admin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'date', 'controler_auth')

admin.site.register(Payment_method, Payment_method_admin)
admin.site.register(Purchase_type, Purchase_type_admin)
admin.site.register(Threshold, Threshold_admin)
admin.site.register(Order, Order_admin)