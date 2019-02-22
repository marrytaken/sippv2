# Generated by Django 2.1.4 on 2018-12-21 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20181221_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=16, verbose_name='任务名称')),
                ('pid', models.IntegerField(verbose_name='任务进程id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User')),
            ],
        ),
        migrations.RenameField(
            model_name='token',
            old_name='username',
            new_name='user',
        ),
    ]
