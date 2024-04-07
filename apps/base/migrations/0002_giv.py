# Generated by Django 5.0.3 on 2024-04-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name=' Giveaway for laptop (title)')),
                ('video', models.FileField(upload_to='image/', verbose_name=' Giveaway for laptop (video)')),
            ],
            options={
                'verbose_name': ' Giveaway for laptop ',
            },
        ),
    ]
