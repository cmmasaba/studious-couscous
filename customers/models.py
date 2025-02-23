from django.db import models
from django.contrib.auth import get_user_model
import json
import os

User = get_user_model()

class Customer(models.Model):
    first_name = models.CharField(max_length=20) # first name of the customer
    last_name = models.CharField(max_length=20) # last name of the customer
    phone = models.CharField(max_length=15, unique=True) # phone number of the customer
    code = models.CharField(max_length=5, unique=True) # unique code for the customer
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    async def asave(self, *args, **kwargs):
        """Overriding the save method to do so asynchronously"""
        await super().asave(*args, **kwargs)
        self.customers = {}
        with open('customers.json', 'r', encoding='utf-8') as file:
            if not os.path.getsize('customers.json') == 0:
                self.customers = json.loads(file.read())
        
        with open('customers.json', 'w', encoding='utf-8') as file:
            name = f'{self.first_name} {self.last_name}'
            code = self.code
            self.customers[code] = name
            json.dump(self.customers, file, indent=4)

    def __str__(self):
        return f"{self.first_name} {self.last_name} -: {self.code}"
    
