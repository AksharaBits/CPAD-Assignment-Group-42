# Generated by Django 4.0.4 on 2022-05-02 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_doctor_id_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DocAvailability',
        ),
    ]
