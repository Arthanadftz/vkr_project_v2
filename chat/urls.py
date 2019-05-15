from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.chat_index, name='index_chat'),
    path('select/', views.chat_select, name='chat_select'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.chat_room, name='chat_room'),
]
