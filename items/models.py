from django.db import models

class Item(models.Model):
    item_id = models.BigAutoField(primary_key=True)  # the unique id of each item
    name = models.CharField(max_length=50)  # the name of the item
    price = models.FloatField()  # the price of the item