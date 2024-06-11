from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer

class CreatePayment(APIView):
    def post(self, request):
        order_id = request.data.get('order_id')
        amount=request.data.get('amount')
        payment_method=request.data.get('payment_method')
        payment = Payment.objects.create(order_id=order_id, amount=amount, payment_method=payment_method)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
