from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Feedback


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

#@login_required
class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')

#@login_required
class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback_detail.html'

#@login_required
class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'feedback_new.html'
    fields = ['name', 'body']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()

        return super().form_valid(form)
