# Generated by Django 2.1.4 on 2019-01-15 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0031_auto_20190115_0414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_sys',
            old_name='countTime',
            new_name='sysTime',
        ),
    ]
