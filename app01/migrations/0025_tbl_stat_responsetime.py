# Generated by Django 2.1.4 on 2019-01-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0024_auto_20190112_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_stat',
            name='responseTime',
            field=models.IntegerField(null=True, verbose_name='响应时间'),
        ),
    ]
