# Generated by Django 3.1.7 on 2021-02-21 07:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210221_0512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='food_name',
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='food_category',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=15), size=5),
        ),
    ]