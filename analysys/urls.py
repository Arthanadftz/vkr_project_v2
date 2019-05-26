from django.urls import path
from . import views


urlpatterns = [
    #path('', views.AnalysysDashBoard.as_view(), name='analysys_dash'),
    #path('', views.ChartCreateView.as_view(), name='new_chart'),
    path('', views.dashboardView, name='dashboard'),
    #path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    #path('<int:pk>/edit/',
    #     views.ArticleUpdateView.as_view(), name='article_edit'),
    #path('<int:pk>/',
    #     views.ArticleDetailView.as_view(), name='article_detail'),
    #path('<int:pk>/delete/',
    #     views.ArticleDeleteView.as_view(), name='article_delete'),
]
