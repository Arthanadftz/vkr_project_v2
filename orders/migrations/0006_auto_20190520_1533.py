# Generated by Django 2.2 on 2019-05-20 12:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190520_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pred_date_rdy',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 12, 33, 31, 573975, tzinfo=utc), verbose_name='Предварительная дата готовности'),
        ),
    ]
