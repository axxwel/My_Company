from django.contrib import admin

from purchases_auth.models import Payment_method, Purchase_type, Process, Order
    
class Payment_method_admin(admin.ModelAdmin):
    list_display = ('name',)

class Purchase_type_admin(admin.ModelAdmin):
    list_display = ('name',)

class Process_admin(admin.ModelAdmin):
    list_display = ('name', 'company_threshold', 'branch_threshold', 'process_threshold')

class Order_admin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'date', 'controler_auth')

admin.site.register(Payment_method, Payment_method_admin)
admin.site.register(Purchase_type, Purchase_type_admin)
admin.site.register(Process, Process_admin)
admin.site.register(Order, Order_admin)