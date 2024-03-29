# Generated by Django 5.0 on 2024-01-03 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_alter_order_options_remove_order_items_order_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="items",
            field=models.ManyToManyField(through="api.OrderItem", to="api.item"),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="api.order",
            ),
        ),
    ]
