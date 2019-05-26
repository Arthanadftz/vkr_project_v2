from django.db import models
from django.urls import reverse
from django.conf import settings


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.json', '.csv', '.jpg', '.png']

    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Рарешение {ext} не поддерживается.')

# Create your models here.
class Chart(models.Model):
    name = models.CharField(max_length=255, default="Название отчета")
    axis_x = models.TextField(verbose_name="Аргументы оси X")
    axis_y = models.TextField(verbose_name="Аргументы оси Y")
    image = models.ImageField(validators=[validate_file_extension], upload_to='analysys/charts/%Y%m%D/', verbose_name="График", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            verbose_name = "Создал"
        )
    def __str__(self):
            return f'{self.name}'

    def get_absolute_url(self):
        return reverse('attendance_detail', args=[str(self.id)])



"""from articles.models import Article
from attendance_control.models import Attendance, Disciple
from chat.models import Message
from orders.models import Order
from questiontest.models import RK, RKResult
from users.models import CustomUser, UserProfile

all_users = CustomUser.objects.filter(pk__gte=2)
all_messages = Message.objects.all()
all_orders = Order.objects.all()
all_rks = RK.objects.all()
all_rk_results = RKResult.objects.all()
all_disciplines = Disciple.objects.all()
all_articles = Article.objects.all()
all_attendance_logs = Attendance.objects.all()

DATA_CHOICES = (
    (all_users, 'USR'),
    (all_messages, 'MSG'),
    (all_orders, 'RKS'),
    (all_rk_results, 'RKR'),
    (all_disciplines, 'DSC'),
    (all_articles, 'ART'),
    (all_attendance_logs, 'ATT'),
)

axis_x = models.CharField(max_length=3,
    choices=DATA_CHOICES,
    verbose_name='Аргументы оси X',
    default=all_orders
)

axis_y = models.CharField(max_length=3,
    choices=DATA_CHOICES,
    verbose_name='Аргументы оси Y',
    default=all_usrers[0].username
)"""
