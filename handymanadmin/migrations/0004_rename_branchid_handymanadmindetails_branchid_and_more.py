# Generated by Django 4.0 on 2022-01-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handymanadmin', '0003_handymanadmindetails_branchid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='handymanadmindetails',
            old_name='branchID',
            new_name='branchId',
        ),
        migrations.AddField(
            model_name='handymanadmindetails',
            name='country',
            field=models.CharField(default='INDIA', max_length=30),
        ),
        migrations.AddField(
            model_name='handymanadmindetails',
            name='stateName',
            field=models.CharField(default='', max_length=30),
        ),
    ]
