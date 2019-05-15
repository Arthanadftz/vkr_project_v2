from django.conf import settings
from django.db import models
from django.urls import reverse

#from datetime import timedelta#, datetime
from django.utils.timezone import timedelta, now
# Create your models here.

class Order(models.Model):
    READY = 'ГТВ'
    WIP = 'ОБР'

    STATUS_CHOICES = (
        (READY, 'Готово'),
        (WIP, 'Обработка')
    )
    status = models.CharField(max_length=3,
        choices=STATUS_CHOICES,
        default=WIP,
        verbose_name='Статус заявки'
    )

    title = models.CharField(max_length=255, verbose_name="Комментарий")
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    pred_date_rdy = models.DateTimeField(verbose_name='Предварительная дата готовности', default=(now() + timedelta(days=3)))
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = "Заказчик"
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])
