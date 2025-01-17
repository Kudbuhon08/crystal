# Generated by Django 5.0.3 on 2024-04-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_giv_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Q&A title')),
                ('questions', models.CharField(max_length=255, verbose_name='questions')),
                ('answers', models.CharField(max_length=255, verbose_name='answers')),
            ],
            options={
                'verbose_name': 'Questions and answers',
            },
        ),
    ]
