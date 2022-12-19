from django.contrib import admin

from purchases_auth.models import Order
    
class Order_admin(admin.ModelAdmin):
    list_display = ('order_id', 'date', 'controler_auth')

admin.site.register(Order, Order_admin)