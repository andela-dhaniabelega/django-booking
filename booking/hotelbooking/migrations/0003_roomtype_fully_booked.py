# Generated by Django 2.0.7 on 2018-09-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0002_auto_20180812_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='fully_booked',
            field=models.BooleanField(default=False),
        ),
    ]
