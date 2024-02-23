from django.test import TestCase

from customers.models import Customer

class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testcustomer = Customer.objects.create(
            first_name='test',
            last_name='user',
            phone='+254791159131',
            code='tu123',
        )
        testcustomer.save()

    def test_customer_first_name(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = f'{customer.first_name}'
        self.assertEqual(expected_object_name, 'test')

    def test_customer_last_name(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = f'{customer.last_name}'
        self.assertEqual(expected_object_name, 'user')

    def test_customer_phone(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = f'{customer.phone}'
        self.assertEqual(expected_object_name, '+254791159131')

    def test_customer_code(self):
        customer = Customer.objects.get(id=1)
        expected_object_name = f'{customer.code}'
        self.assertEqual(expected_object_name, 'tu123')

    #def test_customer_str(self):
    #    customer = Customer.objects.get(id=1)
    #    expected_object_name = f"{customer.first_name} {customer.last_name} -: {customer.code}"
    #    self.assertEqual(expected_object_name, str(customer))
