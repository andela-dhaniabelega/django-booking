# Generated by Django 2.0.7 on 2018-09-09 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0004_auto_20180909_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtype',
            old_name='booking_count',
            new_name='available_count',
        ),
    ]
