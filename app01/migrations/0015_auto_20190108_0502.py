# Generated by Django 2.1.4 on 2019-01-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_auto_20190108_0415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_task',
            old_name='concurrentNum',
            new_name='beginConcurrentNum',
        ),
        migrations.AddField(
            model_name='tbl_task',
            name='taskId',
            field=models.IntegerField(default=1, unique=True, verbose_name='任务id'),
        ),
    ]