# Generated by Django 3.1 on 2022-10-19 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0019_auto_20221019_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seglowcustomer',
            name='customer_phone_no',
        ),
    ]
