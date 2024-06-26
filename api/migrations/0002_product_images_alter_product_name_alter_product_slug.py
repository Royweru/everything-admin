# Generated by Django 4.2.4 on 2024-06-13 03:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1080), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=250),
        ),
    ]
