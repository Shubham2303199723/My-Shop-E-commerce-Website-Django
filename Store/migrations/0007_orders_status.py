# Generated by Django 4.2.2 on 2024-03-27 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_orders_address_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
