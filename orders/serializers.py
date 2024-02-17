from rest_framework import serializers

from orders.models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.name')
    item = serializers.ReadOnlyField(source='item.name')
    
    class Meta:
        model = Order
        fields = ['url', 'id', 'time_placed', 'time_closed', 'quantity', 'status', 'customer', 'item', 'amount']