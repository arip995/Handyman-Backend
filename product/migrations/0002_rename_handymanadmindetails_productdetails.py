# Generated by Django 4.0 on 2022-02-12 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HandymanAdminDetails',
            new_name='ProductDetails',
        ),
    ]
