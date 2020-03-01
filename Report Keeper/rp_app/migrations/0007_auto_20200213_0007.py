# Generated by Django 3.0.3 on 2020-02-12 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rp_app', '0006_createrecord_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createrecord',
            name='complaint_sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='suspect_sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
