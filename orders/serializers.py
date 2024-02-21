from rest_framework import serializers

from orders.models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.__str__')
    
    class Meta:
        model = Order
        fields = ['id', 'item', 'amount', 'quantity', 'price_per_unit', 'status',
                  'customer_code', 'customer','time_placed', 'url',]