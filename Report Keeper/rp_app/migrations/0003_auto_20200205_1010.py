# Generated by Django 3.0.3 on 2020-02-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rp_app', '0002_auto_20200205_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createrecord',
            name='cfa_recieved',
        ),
        migrations.RemoveField(
            model_name='createrecord',
            name='complaint_lga',
        ),
        migrations.RemoveField(
            model_name='createrecord',
            name='complaint_soo',
        ),
        migrations.RemoveField(
            model_name='createrecord',
            name='suspect_lga',
        ),
        migrations.RemoveField(
            model_name='createrecord',
            name='suspect_soo',
        ),
        migrations.AddField(
            model_name='createrecord',
            name='cFA_recieved',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='createrecord',
            name='complaint_LGA',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='createrecord',
            name='complaint_state_of_origin',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='createrecord',
            name='suspect_LGA',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='createrecord',
            name='suspect_state_of_orgin',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='amount_involved_dollar',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='amount_involved_naira',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='amount_recieved_dollar',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='amount_recieved_naira',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='cer_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='cfa_involved',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='complaint_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='complaint_age',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='complaint_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='date_sent_to_legal',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='offence',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='others_involved',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='others_recieved',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='suspect_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='suspect_age',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='createrecord',
            name='suspect_name',
            field=models.CharField(max_length=50),
        ),
    ]
