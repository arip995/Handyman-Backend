# Generated by Django 4.0 on 2022-01-13 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0034_alter_workerinformation_foreignid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerinformation',
            name='key',
        ),
    ]
