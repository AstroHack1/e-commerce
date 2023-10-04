from django.urls import path

from .views import OrderCreateView, CancelTemplateView, SuccessTemplateView, OrderListView, OrderDetailView

app_name = 'orders'

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order_success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order_canceled/', CancelTemplateView.as_view(), name='order_canceled'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('', OrderListView.as_view(), name='orders_list'),
]
