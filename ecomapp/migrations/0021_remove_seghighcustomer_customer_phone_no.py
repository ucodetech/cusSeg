# Generated by Django 3.1 on 2022-10-19 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0020_remove_seglowcustomer_customer_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seghighcustomer',
            name='customer_phone_no',
        ),
    ]
