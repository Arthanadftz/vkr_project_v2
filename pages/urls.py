from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('feedback/', login_required(views.FeedbackListView.as_view()), name='feedback_list'),
    path('feedback/new/', login_required(views.FeedbackCreateView.as_view()), name='feedback_new'),
    path('feedback/<int:pk>/',
         login_required(views.FeedbackDetailView.as_view()), name='feedback_detail'),

]
