# Generated by Django 2.2.13 on 2021-02-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210220_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='food_category',
            field=models.CharField(default='Category', max_length=50),
        ),
    ]
