# Generated by Django 2.1.4 on 2019-01-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0033_auto_20190115_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_sys',
            name='currentCps',
            field=models.FloatField(default=0, verbose_name='当前系统总的cps'),
        ),
    ]
