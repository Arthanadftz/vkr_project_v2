#from django.contrib.auth import get_user_model
#User = get_user_model()
from django.db import models
from users.models import CustomUser


class Message(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_messages', verbose_name="Автор")
    content = models.TextField(verbose_name="Текст сообщения")
    date = models.DateTimeField(auto_now_add=True, verbose_name='Отправлено')

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-date').all()[:10]
