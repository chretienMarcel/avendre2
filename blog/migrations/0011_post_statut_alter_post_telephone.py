# Generated by Django 5.0.6 on 2024-11-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='statut',
            field=models.CharField(choices=[('à louer', 'à louer'), ('à vendre', 'à vendre')], default='à louer', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='telephone',
            field=models.CharField(max_length=12),
        ),
    ]
