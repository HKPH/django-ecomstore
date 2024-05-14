from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shipment
from .serializers import ShipmentSerializer

class CreateShipment(APIView):
    def post(self, request):
        order_id = request.data.get('order_id')
        address = request.data.get('address')
        fee = request.data.get('fee')

        shipment = Shipment.objects.create(order_id=order_id, address=address, fee=fee)

        serializer = ShipmentSerializer(shipment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
