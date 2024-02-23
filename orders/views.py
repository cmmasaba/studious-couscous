from orders.models import Order
from rest_framework import permissions
from orders.permissions import IsOwner
from rest_framework import viewsets

from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'update',
    'retrieve', and 'destroy' actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # only permit authenticated users and owners of the object
    #permission_classes = [permissions.IsAuthenticated,
    #                      IsOwner]
    permission_classes = [permissions.IsAuthenticated,]
    
    def perform_create(self, serializer):
        """Associate the order with the user."""
        serializer.save(owner=self.request.user)
