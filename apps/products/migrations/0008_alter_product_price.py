# Generated by Django 5.0.3 on 2024-04-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='product price'),
        ),
    ]
