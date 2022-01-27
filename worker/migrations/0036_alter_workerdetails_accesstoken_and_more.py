# Generated by Django 4.0 on 2022-01-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0035_remove_workerinformation_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerdetails',
            name='accessToken',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='createdOn',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='firstName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='lastName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='mobileNumber',
            field=models.BigIntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='password',
            field=models.CharField(max_length=500, null=True),
        ),
    ]