# Generated by Django 4.2.3 on 2023-07-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_basket_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='basket_history',
            field=models.JSONField(default=dict),
        ),
    ]
