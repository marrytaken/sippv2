# Generated by Django 2.1.4 on 2018-12-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_sys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currCpu', models.CharField(max_length=8, null=True, verbose_name='当前cpu使用率')),
                ('cpu_status', models.CharField(max_length=8, null=True, verbose_name='cpu状态')),
                ('currMem', models.CharField(max_length=8, null=True, verbose_name='当前Mem使用率')),
                ('mem_status', models.CharField(max_length=8, null=True, verbose_name='cpu状态')),
                ('currDisk', models.CharField(max_length=8, null=True, verbose_name='当前disk使用率')),
                ('disk_status', models.CharField(max_length=8, null=True, verbose_name='cpu状态')),
                ('curr_rx', models.CharField(max_length=8, null=True, verbose_name='当前接收流量')),
                ('rx_status', models.CharField(max_length=8, null=True, verbose_name='上行流量趋势率')),
                ('curr_tx', models.CharField(max_length=8, null=True, verbose_name='当前下行流量')),
                ('tx_status', models.CharField(max_length=8, null=True, verbose_name='下行流量趋势率')),
            ],
        ),
    ]
