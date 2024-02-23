# Generated by Django 5.0.1 on 2024-02-23 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('price_per_unit', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Pending', max_length=10)),
                ('customer_code', models.CharField(max_length=5)),
                ('time_placed', models.DateTimeField(auto_now_add=True)),
                ('time_closed', models.DateTimeField(blank=True, null=True)),
                ('owner', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customers.customer')),
            ],
        ),
    ]