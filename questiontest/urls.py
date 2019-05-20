from django.urls import path
from . import views
#from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.RKListView.as_view(), name='rk_list'),
    path('new/', views.RKCreateView.as_view(), name="rk_new"),
    path('<rk_id>/', views.add_questions, name="question_new"),
    #path('<int:pk>/edit/',
    #     views.ArticleUpdateView.as_view(), name='rk_edit'),
    #path('<int:pk>/',
    #     views.ArticleDetailView.as_view(), name='article_detail'),
]
