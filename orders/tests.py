from django.test import TestCase

from customers.models import Customer
from .models import Order


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testcustomer = Customer.objects.create(
            first_name='test',
            last_name='user',
            phone='+254791159131',
            code='tu123',
        )
        testcustomer.save()

        test_order = Order.objects.create(
            item='Test Item',
            price_per_unit=100,
            quantity=2,
            status='Pending',
            customer_code='tu123',
        )
        test_order.save()
    
    def test_order_item(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.item}'
        self.assertEqual(expected_object_name, 'Test Item')
    
    def test_order_price_per_unit(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.price_per_unit}'
        self.assertEqual(expected_object_name, '100.0')
    
    def test_order_quantity(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.quantity}'
        self.assertEqual(expected_object_name, '2')
    
    def test_order_status(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.status}'
        self.assertEqual(expected_object_name, 'Pending')
    
    def test_order_customer_code(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.customer_code}'
        self.assertEqual(expected_object_name, 'tu123')
    
    def test_order_customer_relationship(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.customer.first_name}'
        self.assertEqual(expected_object_name, 'test')