from django import forms

from purchases_auth.models import Auth_datas

class Order_form(forms.ModelForm):
    class Meta:
        model = Auth_datas
        fields = '__all__'
    