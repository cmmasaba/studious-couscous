from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=20) # first name of the customer
    last_name = models.CharField(max_length=20) # last name of the customer
    phone = models.CharField(max_length=15, unique=True) # phone number of the customer
    code = models.CharField(max_length=5, unique=True) # unique code for the customer

    def __str__(self):
        return f"{self.first_name} {self.last_name} -: {self.code}"
    