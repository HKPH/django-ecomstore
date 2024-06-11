from django.urls import path
from .views import CreatePayment
urlpatterns = [
    path('api/create-payment/', CreatePayment.as_view(), name='create-payment'),
]
