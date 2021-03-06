from django.db import models
from django.utils.timezone import timedelta, now
from django.urls import reverse
from django.conf import settings

from attendance_control.models import Disciple
#from users.models import CustomUser

# Create your models here.

class RK(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название РК", default="РК1")
    disciple = models.ForeignKey(Disciple, on_delete=models.CASCADE, verbose_name="Дисциплина", null=True)
    date_start = models.DateTimeField(default=now, verbose_name='Дата начала')
    date_stop = models.DateTimeField(verbose_name='Дата окончания', default=(now() + timedelta(days=3)))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('question_new', args=[str(self.id)])


class RKResult(models.Model):

    student = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            verbose_name = "Студент"
        )
    #student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Студент", default=0)
    rk = models.ForeignKey(RK, on_delete=models.CASCADE, verbose_name="РК", null=True)
    result = models.CharField(max_length=5, verbose_name="Результат в '%'", default="100%")
    answers = models.CharField(max_length=255, verbose_name="Ответы студента", default="[A, A]")
    date = models.DateTimeField(auto_now=True, verbose_name='Дата выполнения')

    def __str__(self):
        return f"Результат студента, {self.student.full_name}: {self.result}"

    def get_absolute_url(self):
        return reverse('rk_result', args=[str(self.id)])


class Question(models.Model):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

    ANSWERS_CHOICES = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D')
    )

    name = models.CharField(max_length=255, verbose_name="Название вопроса", default="Некоторый вопрос")
    body = models.TextField(verbose_name="Содержание вопроса", default="Выберете правильный вариант ответа...")
    answer_true = models.CharField(max_length=1, choices=ANSWERS_CHOICES, default='A', verbose_name="Вариант правильного ответа")
    rk = models.ForeignKey(RK, on_delete=models.CASCADE, verbose_name="Контрольные вопросы", null=True)

    def __str__(self):
        return self.name




"""class AnswersTest(models.Model):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'

    ANSWERS_CHOICES = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D')
    )

    choices = models.CharField(max_length=1,
        choices=ANSWERS_CHOICES,
        verbose_name='Вариант ответа',
        default=A
        )

    def __str__(self):

    #answers = models.ManyToManyField(AnswersTest, verbose_name="Варианты ответа")
    #questions = models.ForeignKey(QuestionsTest, on_delete=models.CASCADE, verbose_name="Контрольные вопросы")
        return self.choices"""
