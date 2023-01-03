from django import forms

from purchases_auth.models import Order

class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = ['branch', 'process', 'payment_method', 'product', 'price']
        
        #fields = '__all__'
        """ exclude = (
            'order_id',
            'date', 
            'asker_login',
            'controler_login', 
            'controler_auth',
            'controler_comment',
        ) """
    