from django.urls import path
from .views import CreateShipment

urlpatterns = [
    path('create-shipment/', CreateShipment.as_view(), name='create-shipment'),
]
