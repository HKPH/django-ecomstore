from django.db import transaction
from .models import Order, OrderItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
import requests
from decimal import Decimal
class CreateOrderView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('userId')
        shipment_data = request.data.get('shipment')
        payment_data = request.data.get('payment')
        cart_response = requests.get(f'http://localhost:8004/api/cart/get_cart/{user_id}/')
        if cart_response.status_code != status.HTTP_200_OK:
            return Response({"error": "Không thể lấy giỏ hàng của người dùng."}, status=cart_response.status_code)
        cart_items = cart_response.json()
        if not cart_items:
            return Response({"error": "Giỏ hàng của bạn đang trống."}, status=status.HTTP_400_BAD_REQUEST)
        order = Order.objects.create(
            user_id=user_id,
            total_price=0,
            status="Đang xử lý"
        )
        for cart_item in cart_items:
            product_type = cart_item.get('product_type')
            product_id = cart_item.get('product_id')
            price = cart_item.get('price')
            quantity = cart_item.get('quantity')

            OrderItem.objects.create(
                order=order,
                product_type=product_type,
                product_id=product_id,
                price=price,
                quantity=quantity
            )
        order_id=order.id
        shipment_fee = calculate_shipment_fee(order.items.all())
        user_address=shipment_data
        create_shipment(order_id,user_address,shipment_fee)
        total_price = Decimal(sum(Decimal(cart_item.get('price')) * cart_item.get('quantity') for cart_item in cart_items)) + shipment_fee
        order.total_price = total_price
        order.save()
        create_payment(order_id,total_price,payment_data)
        requests.delete(f'http://localhost:8004/api/cart/delete/{user_id}/')
        return Response({"success": "Đã tạo đơn hàng thành công."}, status=status.HTTP_201_CREATED)
    
def create_payment(order_id, amount, payment_method):
    payment_data = {
        'order_id': order_id,
        'amount': amount,
        'payment_method': payment_method
    }
    payment_response = requests.post('http://localhost:8005/api/create-payment', data=payment_data)
    return payment_response
def create_shipment(order_id, address, fee):
    shipment_data = {
        'order_id': order_id,
        'address': address,
        'fee': fee
    }
    shipment_response = requests.post('http://localhost:8007/api/create-shipment/', data=shipment_data)
    return shipment_response
def calculate_shipment_fee(items):
    ship_fee=0
    total_price = sum(item.price * item.quantity for item in items)
    if total_price < 100000:
        ship_fee = 5000
    elif 100000 <= total_price < 500000:
        ship_fee = 10000
    elif 500000 <= total_price < 1000000:
        ship_fee = 20000
    else:
        ship_fee = 30000
    return ship_fee
class OrderView(APIView):
    def get(self, request, user_id):
        try:
            orders = Order.objects.filter(user_id=user_id)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except OrderItem.DoesNotExist:
            return Response({'error': 'No orders found for this user'}, status=status.HTTP_404_NOT_FOUND)
