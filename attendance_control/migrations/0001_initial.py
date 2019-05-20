# Generated by Django 2.2 on 2019-05-20 09:32

import attendance_control.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('ИУ1', 'ИУ-1'), ('ИУ2', 'ИУ-2'), ('ИУ3', 'ИУ-3'), ('ИУ4', 'ИУ-4'), ('ИУ5', 'ИУ-5'), ('ИУ6', 'ИУ-6'), ('ИУ7', 'ИУ-7'), ('ИУ8', 'ИУ-8')], default='ИУ6', max_length=3, verbose_name='Группа студента')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/attendance/%Y%m%D/', validators=[attendance_control.models.validate_file_extension], verbose_name='Файл')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('tmp', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название предмета')),
            ],
        ),
    ]
