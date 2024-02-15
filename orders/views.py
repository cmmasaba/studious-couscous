from orders.models import Order
from rest_framework import permissions
from orders.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'update',
    'retrieve', and 'destroy' actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        """Associate the order with the customer."""
        serializer.save(customer=self.request.user)