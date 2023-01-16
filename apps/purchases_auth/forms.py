from django import forms
import datetime

from purchases_auth.models import Order, Payment_method, Purchase_type, Process

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
    
class PaymentMethodForm(forms.ModelForm):
    add_payment_method = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Payment_method
        fields = [
            'name',
        ]

class PurchaseTypeForm(forms.ModelForm):
    add_purchase_type = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Purchase_type
        fields = [
            'name',
        ]

class ProcessForm(forms.ModelForm):
    add_processs_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Process
        fields = [
            'name',
            'company',
            'branch',
            'Purchase_type',
            'company_threshold',
            'branch_threshold',
            'process_threshold',
        ]