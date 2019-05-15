from django.conf import settings
from django.db import models
from django.urls import reverse
# Create your models here.
import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.txt', '.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']

    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Рарешение {ext} не поддерживается.')


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст")
    document = models.FileField(validators=[validate_file_extension], verbose_name="Файл", blank=True, null=True, upload_to="documents") #/%Y%m%D/
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Автор"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
