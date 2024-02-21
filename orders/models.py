from django.db import models
from customers.models import Customer

from .send_sms import send_sms

ORDER_STATUS = {
    'Pending': 'Pending',
    'Cancelled': 'Cancelled',
    'Completed': 'Completed'
}

# Create your models here.
class Order(models.Model):
    item = models.TextField()  # the item in the order
    price_per_unit = models.FloatField()  # the price of the item
    quantity = models.IntegerField()  # the number of items in the order
    status = models.CharField(choices=ORDER_STATUS, default='Pending',
                              max_length=10)  # the lifecycle of the order
    customer_code = models.CharField(max_length=5)  # the customer's code
    # time_placed is a required field and is automatically set to the current time when the order is created
    time_placed = models.DateTimeField(auto_now_add=True)
    time_closed = models.DateTimeField(null=True, blank=True)  # record when the order is closed

    # create a many-to-one relationship with the custoners model. 
    # Many orders can belong to one customer
    customer = models.ForeignKey('customers.Customer',
                                 related_name='orders', on_delete=models.CASCADE)
    # similarly a many-to-one relationship with items model.
    # An order can only contain a single item but one item can be in multiple orders
    # item = models.ForeignKey('items.Item',
    #                         related_name='item_orders', on_delete=models.CASCADE)

    @property
    def amount(self) -> float:
        """Calculate the amount from the quantity and item.
        
        Return the total amount.
        """
        return self.quantity * self.price
    
    def save(self, *args, **kwargs):
        """Override the save method to send an SMS when the order is placed."""
        self.customer = Customer.objects.get(code=self.customer_code)
        send_sms([self.customer.phone], f"Greetings {self.customer.first_name}. \
                 Your order of {self.quantity} {self.item} has been placed at {self.time_placed}.\
                 Thank you for choosing SIL.")
        super().save(*args, **kwargs)