# Generated by Django 5.0.3 on 2024-04-05 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/', verbose_name='photo (configurations)')),
            ],
            options={
                'verbose_name': 'Products image',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_products', to='products.productimage'),
        ),
    ]
