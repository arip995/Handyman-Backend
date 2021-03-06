# Generated by Django 4.0 on 2022-01-13 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0032_alter_workerinformation_foreignid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerinformation',
            name='foreignId',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='worker.workerdetails'),
        ),
        migrations.AlterField(
            model_name='workerinformation',
            name='key',
            field=models.IntegerField(editable=False, unique=True),
        ),
    ]
