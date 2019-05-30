from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone

from .models import Chart
from articles.models import Article
from attendance_control.models import Attendance, Disciple
from chat.models import Message
from orders.models import Order
from questiontest.models import RK, RKResult
from users.models import CustomUser, UserProfile
from pages.models import Feedback
# Create your views here.

"""def create_chart(request):
    all_users = CustomUser.objects.filter(pk__gte=2)
    all_messages = Message.objects.all()
    all_orders = Order.objects.all()
    all_rks = RK.objects.all()
    all_rk_results = RKResult.objects.all()
    all_disciplines = Disciple.objects.all()
    all_articles = Article.objects.all()
    all_attendance_logs = Attendance.objects.all()"""

"""
class ChartListView(ListView):
    model = Chart
    template_name = 'chart_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class ChartDetailView(DeleteView):
    model = Chart
    template_name = 'chart_detail.html'
"""


class ChartCreateView(CreateView):
    model = Chart
    template_name = 'chart_new.html'
    fields = ['name', 'axis_x', 'axis_y']

    def get_context_data(self, *args, **kwargs):
        all_users = CustomUser.objects.all()
        all_messages = Message.objects.all()
        all_orders = Order.objects.all()
        all_rks = RK.objects.all()
        all_rk_results = RKResult.objects.all()
        all_disciplines = Disciple.objects.all()
        all_articles = Article.objects.all()
        all_attendance_logs = Attendance.objects.all()

        context = super(ChartCreateView, self).get_context_data(*args, **kwargs)
        context['users'] = all_users
        context['messages'] = all_messages
        context['disciples'] = all_disciplines
        context['articles'] = all_articles

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        #obj.image = '.jpg'
        obj.save()

        return super().form_valid(form)


def dashboardView(request):
    # Get all data
    all_students = CustomUser.objects.filter(user_role=CustomUser.STUDENT)
    all_teachers = CustomUser.objects.filter(user_role=CustomUser.TEACHER)
    all_messages = Message.objects.all()
    all_orders = Order.objects.all()
    all_rks = RK.objects.all()
    all_rk_results = RKResult.objects.all()
    all_disciplines = Disciple.objects.all()
    all_articles = Article.objects.all()
    all_attendance_logs = Attendance.objects.all()
    all_feedbacks = Feedback.objects.all()
    # Prepare data
    #context = super(ChartCreateView, self).get_context_data(*args, **kwargs)
    orders_count = len(all_orders)
    students_count = len(all_students)
    teachers_count = len(all_teachers)
    feedbacks_count = len(all_feedbacks)

    students_age = [int(timezone.now().year - el.date_of_birth.year) for el in all_students]
    avg_age = sum(students_age)//students_count

    all_teacher_discs = [", ".join([el.name for el in teacher.disciple_set.all()]) for teacher in all_teachers]
    #all_teacher_discs = []

    #for teacher in all_teachers:
    #    all_teacher_discs.append(", ".join([el.name for el in teacher.disciple_set.all()]))

    teachers_age = [int(timezone.now().year - el.date_of_birth.year) for el in all_teachers]
    avg_age_teacher = sum(teachers_age)//teachers_count

    students_rk_results = []
    students_rk_results_avgs = []
    for student in all_students:
        results = student.rkresult_set.all()
        #if results:
        results_repr = ", ".join([el.result for el in results])
        students_rk_results.append(results_repr)
        students_rk_results_avgs.append(round(sum([float(el.result.split()[0]) for el in results])/len(students_rk_results), 2))

    students_all_avg = round(sum(students_rk_results_avgs)/students_count, 2)

    articles_count = len(all_articles)
    articles_dates_formated = []
    for el in all_articles:
        minute = el.date.minute
        hour = el.date.hour
        day = el.date.day
        year = el.date.year
        month = el.date.month

        if len(str(el.date.month)) == 2:
            articles_dates_formated.append(f"{year}/{month}/{day} {hour}:{minute}")
        else:
            articles_dates_formated.append(f"{year}/0{month}/{day} {hour}:{minute}")


    context = {
        'students': all_students,
        'students_ages': zip(all_students, students_age),
        #'students_rk_results_avgs': zip(students_rk_results, students_rk_results_avgs),
        'students_ages_rk_results_avgs': zip(all_students, students_age, students_rk_results, students_rk_results_avgs),
        'students_count': students_count,
        'students_all_avg': students_all_avg,
        'teachers': zip(all_teachers, teachers_age, all_teacher_discs),
        'teachers_count': teachers_count,
        'avg_age': avg_age,
        'avg_age_teacher': avg_age_teacher,
        'orders': all_orders,
        'orders_count': orders_count,
        'messages': all_messages,
        'disciples': all_disciplines,
        'articles': zip(all_articles, articles_dates_formated),
        'articles_count': articles_count,
        'feedbacks': all_feedbacks,
        'feedbacks_count': feedbacks_count,
        }


    return render(request, 'dashboard.html', context=context)
