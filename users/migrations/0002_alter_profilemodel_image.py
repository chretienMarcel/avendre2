# Generated by Django 5.0.6 on 2024-11-07 05:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(default='default.webp', upload_to='profile', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])]),
        ),
    ]
