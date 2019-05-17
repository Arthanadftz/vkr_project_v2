from django.urls import path
from . import views
#from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.AttendanceListView.as_view(), name='attendance_list'),
    path('new/', views.AttendanceCreateView.as_view(), name='attendance_new'),
    path('<int:pk>/',
         views.AttendanceDetailView.as_view(), name='attendance_detail'),
]
