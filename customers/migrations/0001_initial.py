# Generated by Django 5.0.1 on 2024-02-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('code', models.CharField(max_length=5, unique=True)),
                ('owner', models.TextField()),
            ],
        ),
    ]
