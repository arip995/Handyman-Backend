# Generated by Django 4.0 on 2022-01-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0022_workerinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerinformation',
            name='bankDetails',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='workerinformation',
            name='familyDetails',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='workerinformation',
            name='kyc',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='workerinformation',
            name='personalDetails',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='workerinformation',
            name='residenceDetails',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='workerinformation',
            name='workDetails',
            field=models.JSONField(null=True),
        ),
    ]
