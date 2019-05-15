# Generated by Django 2.2 on 2019-04-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190427_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='student_group',
            field=models.CharField(choices=[('ИУ1', 'ИУ-1'), ('ИУ2', 'ИУ-2'), ('ИУ3', 'ИУ-3'), ('ИУ4', 'ИУ-4'), ('ИУ5', 'ИУ-5'), ('ИУ6', 'ИУ-6'), ('ИУ7', 'ИУ-7'), ('ИУ8', 'ИУ-8')], default='ИУ6', max_length=3, verbose_name='Группа студента'),
        ),
    ]
