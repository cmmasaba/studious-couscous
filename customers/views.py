from customers.models import Customer
from rest_framework import permissions
from customers.permissions import IsAuthorOrViewOnly

from rest_framework import viewsets

from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'update',
    'retrieve', and 'destroy' actions.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorOrViewOnly
    ]
    
    """def perform_create(self, serializer):
        '''Associate the customer with the user who created it.'''
        serializer.save(owner=self.request.user)"""