# Generated by Django 3.0.14 on 2023-08-15 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market_place', '0035_otp_confirmation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r_attribute',
            name='date_of_registration',
        ),
    ]
