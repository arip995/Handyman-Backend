# Generated by Django 4.0 on 2022-01-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0015_alter_workerdetails_mobilenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerdetails',
            name='name',
        ),
        migrations.AddField(
            model_name='workerdetails',
            name='firstName',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='workerdetails',
            name='lastName',
            field=models.CharField(default='', max_length=30),
        ),
    ]
