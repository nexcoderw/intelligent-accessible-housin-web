# Generated by Django 5.0.4 on 2025-04-30 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_alter_contract_rent_application'),
        ('frontend', '0004_remove_rentapplication_property_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RentApplication',
        ),
    ]
