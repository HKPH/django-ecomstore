from django.urls import path
from .views import CreateOrderView, OrderView

urlpatterns = [
    path('api/orders/create/', CreateOrderView.as_view(), name='create-order'),  # Đảm bảo có dấu '/' ở cuối
    path('api/order/<int:user_id>/', OrderView.as_view(), name='order'),
]
