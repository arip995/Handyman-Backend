# Generated by Django 4.0 on 2022-01-05 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_workerdetails_address_workerdetails_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerdetails',
            name='address',
        ),
        migrations.RemoveField(
            model_name='workerdetails',
            name='city',
        ),
        migrations.RemoveField(
            model_name='workerdetails',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='workerdetails',
            name='state',
        ),
    ]
