# Generated by Django 2.2 on 2019-05-21 12:06

import analysys.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Название отчета', max_length=255)),
                ('axis_x', models.TextField(verbose_name='Аргументы оси X')),
                ('axis_y', models.TextField(verbose_name='Аргументы оси Y')),
                ('image', models.ImageField(blank=True, null=True, upload_to='analysys/charts/%Y%m%D/', validators=[analysys.models.validate_file_extension], verbose_name='График')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создал')),
            ],
        ),
    ]