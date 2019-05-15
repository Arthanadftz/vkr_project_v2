from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')

class ArticleDetailView(DeleteView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body', 'document']
    template_name = 'article_edit.html'

    def form_valid(self, form):
        #doc = self.request.body.decode('utf-8').split("&")[-1].split('=')[-1]

        obj = form.save(commit=False)
        #obj.document = self.request.FILES
        obj.save()

        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'body', 'document']

    def form_valid(self, form):
        #doc = self.request.body.decode('utf-8').split("&")[-1].split('=')[-1]
        obj = form.save(commit=False)
        obj.author = self.request.user
        #obj.document = self.request.FILES
        obj.save()

        return super().form_valid(form)
