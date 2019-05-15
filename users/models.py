from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.utils import timezone
from datetime import date

#from student_group.models import Student_group

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateTimeField(verbose_name='Дата рождения', default=date.today)
    full_name = models.CharField(max_length=255, verbose_name='ФИО', null=True)
    phone_no = models.CharField(max_length=255, verbose_name='Контактный телефон', default='+7-499-555-55-55')

    STUDENT = 'СТ'
    TEACHER = 'ПР'

    ROLE_CHOICES = (
        (STUDENT, 'Студент'),
        (TEACHER, 'Преподаватель')
    )
    user_role = models.CharField(max_length=2,
        choices=ROLE_CHOICES,
        default=STUDENT,
        verbose_name='Роль пользователя'
    )

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
    student_group = models.CharField(max_length=3,
        choices=STUDENT_GROUP_CHOICES,
        verbose_name='Группа студента',
        default=IU6
    )

    """
    if user_role == STUDENT:
        user_group = ForeignKey(
        Student_group,
        on_delete=models.CASCADE,
        verbose_name = "Группа студента"
    )
    """

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(upload_to='profile_pics', default='default.jpg', verbose_name='Аватар')

    def __str__(self):
        return f'Профиль пользователя - {self.user.username}'


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
