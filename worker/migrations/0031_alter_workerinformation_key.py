# Generated by Django 4.0 on 2022-01-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0030_workerinformation_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerinformation',
            name='key',
            field=models.IntegerField(unique=True),
        ),
    ]