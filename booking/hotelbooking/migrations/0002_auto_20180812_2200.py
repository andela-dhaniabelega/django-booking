# Generated by Django 2.0.7 on 2018-08-12 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='room',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
