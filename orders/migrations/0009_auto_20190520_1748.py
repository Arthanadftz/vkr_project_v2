# Generated by Django 2.2 on 2019-05-20 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190520_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pred_date_rdy',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 14, 48, 48, 505901, tzinfo=utc), verbose_name='Предварительная дата готовности'),
        ),
    ]
