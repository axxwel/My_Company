from rest_framework.serializers import ModelSerializer
 
from purchases_auth.models import Order
 
class OrderSerializer(ModelSerializer):
 
    class Meta:
        model = Order
        fields = ['order_id', 'asker_login']