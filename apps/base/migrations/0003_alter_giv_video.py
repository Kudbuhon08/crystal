# Generated by Django 5.0.3 on 2024-04-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_giv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giv',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='image/', verbose_name=' Giveaway for laptop (video)'),
        ),
    ]