# Generated by Django 4.2.3 on 2023-09-12 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_striple_product_price_id_product_stripe_product_price_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='product_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='basket',
            name='product_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='basket',
            name='product_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='basket',
            name='quantity_en',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='basket',
            name='quantity_ru',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='basket',
            name='quantity_uz',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='name_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='name_uz',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
