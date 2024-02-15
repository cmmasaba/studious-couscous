from django.db import models

ORDER_STATUS = ('Pending', 'Cancelled', 'Completed')

# Create your models here.
class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    time_placed = models.DateTimeField()  # record when the order is placed
    time_closed = models.DateTimeField()  # record when the order is closed
    quantity = models.IntegerField()  # the number of items in the order
    status = models.CharField(choices=ORDER_STATUS, default='Pending',
                              max_length=10)  # the lifecycle of the order

    # create a many-to-one relationship with the custoners model. 
    #Many orders can belong to one customer
    customer = models.ForeignKey('customers.Customer',
                                 relation_name='orders', on_delete=models.CASCADE)
    # similarly a many-to-one relationship with items model.
    # An order can only contain a single item but one item can be in multiple orders
    item = models.ForeignKey('items.Items',
                             relation_name='orders', on_delete=models.CASCADE)

    @property
    def amount(self) -> float:
        """Calculate the amount from the quantity and item.
        
        Return the total amount.
        """
        return self.quantity * self.item.price