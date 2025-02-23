from django.db import models
import json
import os

class Item(models.Model):
    item_code = models.BigAutoField(primary_key=True)  # the unique id of each item
    item_name = models.CharField(max_length=50)  # the name of the item
    price = models.FloatField()  # the price of the item

    async def asave(self, *args, **kwargs):
        """Overriding the save method to do so asynchronously"""
        await super().asave(*args, **kwargs)
        self.items = {}
        with open('items.json', 'r', encoding='utf-8') as file:
            if not os.path.getsize('items.json') == 0:
                self.items = json.loads(file.read())

        with open('items.json', 'w', encoding='utf-8') as file:
            self.items[self.item_code] = self.item_name
            json.dump(self.items, file, indent=4)