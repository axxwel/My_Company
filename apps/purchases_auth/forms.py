from django import forms
import datetime

from purchases_auth.models import Order

from decimal import Decimal

class Order_form(forms.ModelForm):
    delivery_date=forms.DateField(initial=datetime.date.today ,widget=forms.SelectDateWidget)

    class Meta:
        model = Order
        fields = [
            'branch',
            'process',
            'purchase_type',
            'payment_method',
            'product',
            'unit_price',
            'price',
            'vendor',
            'delivery_date',
            'asker_comment',
        ]

class Order_auth(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'controler_comment',
            'controler_auth',
        ]
    