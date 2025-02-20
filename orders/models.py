from django.db import models
from django.contrib.auth import get_user_model

from customers.models import Customer
from items.models import Item
import json
import os

from .tasks import send_sms

customers_file = 'customers.json'
items_file = 'items.json'

ORDER_STATUS = {
    'Pending': 'Pending',
    'Cancelled': 'Cancelled',
    'Completed': 'Completed'
}
CUSTOMERS = {}
ITEMS = {}

with open(customers_file, 'r') as file:
    # check ifthe file is empty and leave CUSTOMERS dict as is
    if os.path.getsize(customers_file) == 0:
        pass
    else:
        # read from the json file and append the values in the CUSTOMERS dict
        customers = json.loads(file.read())
        for key, value in customers.items():
            CUSTOMERS[key] = value

with open(items_file, 'r') as file:
    # check if file is empty and leave ITEMS dict as is
    if os.path.getsize(items_file) == 0:
        pass
    else:
        # read from the json file and append the values in the ITEMS dict
        items = json.loads(file.read())
        for key, value in items.items():
            ITEMS[key] = value

# Create your models here.
class Order(models.Model):
    item = models.CharField(choices=ITEMS)  # the item in the order
    price_per_unit = models.FloatField()  # the price of the item
    quantity = models.IntegerField()  # the number of items in the order
    status = models.CharField(choices=ORDER_STATUS, default='Pending',
                              max_length=10)  # the lifecycle of the order
    customer_code = models.CharField(choices=CUSTOMERS,)  # the customer's code
    # time_placed is a required field and is automatically set to the current time when the order is created
    time_placed = models.DateTimeField(auto_now_add=True)
    time_closed = models.DateTimeField(null=True, blank=True)  # record when the order is closed
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # create a many-to-one relationship with the custoners model. 
    # Many orders can belong to one customer
    customer = models.ForeignKey('customers.Customer',
                                 related_name='my_orders', on_delete=models.CASCADE)
    # similarly a many-to-one relationship with items model.
    # An order can only contain a single item but one item can be in multiple orders
    # item = models.ForeignKey('items.Item',
    #                         related_name='item_orders', on_delete=models.CASCADE)

    @property
    def amount(self) -> float:
        """Calculate the amount from the quantity and item.
        
        Return the total amount.
        """
        item = Item.objects.get(item_code=self.item)
        return self.quantity * item.price
    
    def save(self, *args, **kwargs):
        """Override the save method to send an SMS when the order is placed."""

        self.customer = Customer.objects.get(code=self.customer_code)

        if self.item == 1:
            send_sms(self.customer.phone, f"Hi {self.customer.first_name}. \
                    Your order of {self.quantity} {self.item} has been placed.\
                    Thank you for choosing SIL.")
        elif self.item > 1:
            send_sms(self.customer.phone, f"Hi {self.customer.first_name}. \
                    Your order of {self.quantity} {self.item}s has been placed.\
                    Thank you for choosing SIL.")