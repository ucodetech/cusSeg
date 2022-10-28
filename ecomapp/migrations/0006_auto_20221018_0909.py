# Generated by Django 3.1 on 2022-10-18 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecomapp.customer'),
        ),
    ]
