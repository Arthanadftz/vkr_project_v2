from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.files import File

from time import time
import json
import pandas as pd
import ast
import os

from .models import Attendance, Disciple
from users.models import CustomUser


class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')

class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = 'attendance_detail.html'


"""
class AttendanceCreateView(CreateView):
    model = Attendance
    template_name = 'attendance_new.html'
    fields = ['title', 'document']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.date = timezone.now()
        obj.save()

        return super().form_valid(form)
"""


class AttendanceCreateView(CreateView):
    model = Attendance
    template_name = 'attendance_new.html'
    fields = ['group', 'disciple', 'tmp']

    def get_context_data(self, *args, **kwargs):
        groups_choices = [
            'ИУ1',
            'ИУ2',
            'ИУ3',
            'ИУ4',
            'ИУ5',
            'ИУ6',
            'ИУ7',
            'ИУ8',
        ]


        context = super(AttendanceCreateView, self).get_context_data(*args, **kwargs)
        context['students'] = CustomUser.objects.filter(student_group='ИУ6', user_role='СТ', pk__gte=2)
        context['disciples'] = Disciple.objects.all()
        context['groups'] = groups_choices
        #white_file_path = os.path.join(settings.MEDIA_ROOT, 'white_power.png')
        #context['white_pow'] = white_file_path
        #print(context.get('white_pow'))

        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.date = timezone.now()

        fname = f'Журнал-{obj.disciple.name}-{timezone.now()}_m.csv'
        fdir = 'attendance_control/atts_csv/{fn}'
        #print(fname)
        form_data = dict(ast.literal_eval(self.request.POST.get('tmp')))
        #print(form_data, type(form_data))
        df = pd.DataFrame(
            {
                "ФИО студента": form_data.get("student"),
                "Присутствие": form_data.get("check")
                }
            )

        df.to_csv(fdir.format(fn=fname))
        #print(df)
        #Process form_data; mk csv_file based on it; save it to obj.document
        with open(fdir.format(fn=fname)) as f:
            my_file = File(f)
            obj.document.save(fname, my_file)

        #os.system("cd attendance_control/atts_csv/ && pwd && rm *.csv")
        os.system(f"cd {fdir[:-4]} && rm *.csv")

        obj.save()
        #print(form, dir(form))

        return super().form_valid(form)
