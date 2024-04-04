from rest_framework import serializers

from orders.models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.__str__')
    owner = serializers.ReadOnlyField(source='owner.username')
    
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be  greater than 1")
        return value
    
    def validate_price_per_unit(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price per unit must be  greater than 1")
        return value

    class Meta:
        model = Order
        fields = ['id', 'item', 'amount', 'quantity', 'price_per_unit', 'status',
                  'customer_code', 'customer','time_placed', 'owner']