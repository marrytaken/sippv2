# Generated by Django 2.1.4 on 2019-01-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_auto_20190108_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_task',
            name='lastForCallTime',
            field=models.IntegerField(null=True, verbose_name='呼叫时长'),
        ),
        migrations.AlterField(
            model_name='tbl_task',
            name='localControlPort',
            field=models.IntegerField(null=True, verbose_name='本地远程控制端口'),
        ),
    ]
