# Generated by Django 4.0 on 2022-01-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0012_alter_workerdetails_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerdetails',
            name='worktype',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
