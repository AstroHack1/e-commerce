# Generated by Django 4.2.3 on 2023-10-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_basket_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='basket_history',
            field=models.CharField(max_length=250),
        ),
    ]
