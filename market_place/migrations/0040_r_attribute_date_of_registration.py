# Generated by Django 3.0.14 on 2023-08-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_place', '0039_auto_20230815_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='r_attribute',
            name='date_of_registration',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
