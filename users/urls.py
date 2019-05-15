from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('user_profile/', views.user_profile_view, name='user_profile'),
    #path('user_profile/', views.UserProfileView.as_view(), name='user_profile'),
]
