# Generated by Django 4.0 on 2022-01-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0005_remove_workerdetails_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerdetails',
            name='worktype',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
