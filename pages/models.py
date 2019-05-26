from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название обращения")
    body = models.TextField(verbose_name="Текст обращения")
    date = models.DateTimeField(auto_now=True, verbose_name="Дата обращения")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Создал"
    )

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('feedback_detail', args=[str(self.id)])
