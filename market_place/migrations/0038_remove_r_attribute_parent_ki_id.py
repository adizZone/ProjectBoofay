# Generated by Django 3.0.14 on 2023-08-15 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market_place', '0037_r_attribute_parent_ki_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r_attribute',
            name='parent_ki_id',
        ),
    ]
