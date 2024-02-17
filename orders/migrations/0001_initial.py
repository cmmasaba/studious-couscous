# Generated by Django 5.0.1 on 2024-02-16 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_placed', models.DateTimeField()),
                ('time_closed', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Pending', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_orders', to='customers.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_orders', to='items.item')),
            ],
        ),
    ]