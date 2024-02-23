from customers.models import Customer
from rest_framework import permissions
from customers.permissions import IsOwner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'update',
    'retrieve', and 'destroy' actions.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # only permit authenticated users and owners of the object
    #permission_classes = [permissions.IsAuthenticated,
    #                      IsOwner]
    permission_classes = [permissions.IsAuthenticated,]
    
    def perform_create(self, serializer):
        """Associate the customer with the user who created it."""
        serializer.save(owner=self.request.user)


"""Defning the api root"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'customers': reverse('customer-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format)
    })
