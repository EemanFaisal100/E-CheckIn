# Generated by Django 5.1.1 on 2024-11-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='check_in',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentattendance',
            name='check_out',
            field=models.TimeField(blank=True, null=True),
        ),
    ]