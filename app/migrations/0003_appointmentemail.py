# Generated by Django 3.2.3 on 2021-05-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_phoneno_patient_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
    ]
