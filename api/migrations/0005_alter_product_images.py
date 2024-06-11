# Generated by Django 4.2.4 on 2024-06-11 07:27

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.JSONField(blank=True, default=api.models.default_list),
        ),
    ]
