# Generated by Django 4.0 on 2022-01-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0037_alter_workerdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerdetails',
            name='firstName',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='lastName',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='password',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='username',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='workerdetails',
            name='worktype',
            field=models.CharField(default='', max_length=30),
        ),
    ]