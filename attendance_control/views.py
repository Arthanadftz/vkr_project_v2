from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone

from time import time
import json

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
    fields = ['group', 'disciple']

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
        context['students'] = CustomUser.objects.filter(student_group='ИУ6')
        context['disciples'] = Disciple.objects.all()
        context['groups'] = groups_choices

        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.date = timezone.now()
        #obj.disciple =


        fname = f'Журнал-{obj.disciple.name}-{timezone.now()}.csv'
        #print(fname)
        form_data = self.request.POST
        print(form_data)

        #Process form_data; mk csv_file based on it; save it to obj.document

        #obj.document = doc

        obj.save()
        print(form, dir(form))

        return super().form_valid(form)
