from django.urls import path
from .views import CreateOrderAPIView,OrderView

urlpatterns = [
    path('api/orders/create', CreateOrderAPIView.as_view(), name='create-order'),
    path('api/order/<int:user_id>/', OrderView.as_view(), name='order'),
    
]
