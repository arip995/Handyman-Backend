# Generated by Django 4.0 on 2022-01-12 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0031_alter_workerinformation_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerinformation',
            name='foreignId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='worker.workerdetails'),
        ),
    ]
