from django.urls import path
from . import views
#from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.RKListView.as_view(), name='rk_list'),
    path('new/', views.RKCreateView.as_view(), name="rk_new"),
    path('<rk_id>/', views.add_questions, name="question_new"),
    path('<rk_id>/solving/', views.rk_solving, name="rk_solving"),
    #path('<rk_id>/results', views.RKResultsListView.as_view(), name="rk_results_list"),
    path('<rk_id>/results', views.RKResultsList, name="rk_results_list"),
    #path('results/<int:pk>', views.RKResultView.as_view(), name="rk_result"),
    path('results/<int:pk>', views.RKResultDetail, name="rk_result"),
]
