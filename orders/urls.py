from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='orders_list'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order_edit'),
    path('new/', views.OrderCreateView.as_view(), name='order_new'),
]
