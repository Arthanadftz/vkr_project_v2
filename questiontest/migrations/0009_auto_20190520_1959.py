# Generated by Django 2.2 on 2019-05-20 16:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questiontest', '0008_auto_20190520_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='rkresult',
            name='answers',
            field=models.CharField(default='[A, A]', max_length=255, verbose_name='Ответы студента'),
        ),
        migrations.AlterField(
            model_name='rk',
            name='date_stop',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 16, 59, 51, 133962, tzinfo=utc), verbose_name='Дата окончания'),
        ),
    ]
