from rest_framework import serializers

from customers.models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, view_name='order-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='customer-detail', format='html')

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name','phone', 'code', 'orders', 'url',]