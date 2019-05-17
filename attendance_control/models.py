from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
import os
from django.core.exceptions import ValidationError

from users.models import CustomUser

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['json', 'csv', 'jpg']

    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Рарешение {ext} не поддерживается.')


"""
class Attendance(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    document = models.FileField(verbose_name="Файл", blank=True, null=True, upload_to="documents/attendance/%Y%m%D/") #/%Y%m%D/  validators=[validate_file_extension],
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Создал"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('attendance_detail', args=[str(self.id)])

"""


class Disciple(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название предмета')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Преподаватель")

    def __str__(self):
        return self.name


class Attendance(models.Model):
    IU1 = 'ИУ1'
    IU2 = 'ИУ2'
    IU3 = 'ИУ3'
    IU4 = 'ИУ4'
    IU5 = 'ИУ5'
    IU6 = 'ИУ6'
    IU7 = 'ИУ7'
    IU8 = 'ИУ8'

    STUDENT_GROUP_CHOICES = (
        (IU1, 'ИУ-1'),
        (IU2, 'ИУ-2'),
        (IU3, 'ИУ-3'),
        (IU4, 'ИУ-4'),
        (IU5, 'ИУ-5'),
        (IU6, 'ИУ-6'),
        (IU7, 'ИУ-7'),
        (IU8, 'ИУ-8')
    )

    group = models.CharField(max_length=3,
        choices=STUDENT_GROUP_CHOICES,
        verbose_name='Группа студента',
        default=IU6
    )
    disciple = models.ForeignKey(Disciple, on_delete=models.CASCADE, verbose_name="Дисциплина", null=True)
    document = models.FileField(verbose_name="Файл", blank=True, null=True, upload_to="documents/attendance/%Y%m%D/",  validators=[validate_file_extension])
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Создал"
    )

    def __str__(self):
        return f'{self.disciple}-{self.date}'

    def get_absolute_url(self):
        return reverse('attendance_detail', args=[str(self.id)])
