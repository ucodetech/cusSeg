# Generated by Django 3.1 on 2022-10-18 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0016_auto_20221018_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transantion',
            name='orderid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecomapp.order'),
        ),
    ]
