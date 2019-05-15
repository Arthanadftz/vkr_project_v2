from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Order

from datetime import timedelta
# Create your views here.


class OrderListView(ListView):
    model = Order
    template_name = 'orders_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def form_valid(self, form):

        obj = form.save(commit=False)
        obj.save()

        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['status']
    template_name = 'order_edit.html'

    def form_valid(self, form):

        obj = form.save(commit=False)
        obj.save()

        return super().form_valid(form)


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_new.html'
    fields = ['title']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        #obj.pred_date_rdy = obj.date + timedelta(days=3)
        #obj.group = self.request.user.student_group
        obj.save()

        return super().form_valid(form)
