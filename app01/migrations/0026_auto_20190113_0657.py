# Generated by Django 2.1.4 on 2019-01-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0025_tbl_stat_responsetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_stat',
            name='countTime',
            field=models.CharField(max_length=19, null=True, verbose_name='数据生成时间'),
        ),
        migrations.AlterField(
            model_name='tbl_task',
            name='endTime',
            field=models.CharField(max_length=19, null=True, verbose_name='任务结束时间'),
        ),
        migrations.AlterField(
            model_name='tbl_task',
            name='startTime',
            field=models.CharField(max_length=19, null=True, verbose_name='任务创建时间'),
        ),
    ]
