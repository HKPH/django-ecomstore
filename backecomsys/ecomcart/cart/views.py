from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartItemSerializer

class AddToCart(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        product_type = request.data.get('product_type')
        product_id = request.data.get('product_id')
        price = request.data.get('price')

        cart, created = Cart.objects.get_or_create(user_id=user_id)

        existing_item = CartItem.objects.filter(cart=cart, product_type=product_type, product_id=product_id).first()

        if existing_item:
            existing_item.quantity += 1
            existing_item.save()
        else:
            new_item = CartItem(cart=cart, product_type=product_type, product_id=product_id, price=price, quantity=1)
            new_item.save()

        return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_201_CREATED)
class RemoveFromCart(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        product_type = request.data.get('product_type')
        product_id = request.data.get('product_id')
        price = request.data.get('price')


        cart, created = Cart.objects.get_or_create(user_id=user_id)

        existing_item = CartItem.objects.filter(cart=cart, product_type=product_type, product_id=product_id).first()

        if existing_item:
            if existing_item.quantity > 1:
                existing_item.quantity -= 1
                existing_item.save()
            else:
                existing_item.delete()
        else:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Product remove from successfully'}, status=status.HTTP_201_CREATED)
class RemoveAllFromCart(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        product_type = request.data.get('product_type')
        product_id = request.data.get('product_id')
        price = request.data.get('price')


        cart, created = Cart.objects.get_or_create(user_id=user_id)

        existing_item = CartItem.objects.filter(cart=cart, product_type=product_type, product_id=product_id).first()

        if existing_item:
                existing_item.delete()
        else:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Product remove from successfully'}, status=status.HTTP_201_CREATED)
    
class CartView(APIView):
    def get(self, request, user_id):

        try:
            cart = Cart.objects.get(user_id=user_id)
            cart_items = CartItem.objects.filter(cart=cart)
            serializer = CartItemSerializer(cart_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart is empty'}, status=status.HTTP_200_OK)
class GetCartByUserId(APIView):
    def get(self, request, user_id):
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response({"error": "Không tìm thấy giỏ hàng của người dùng."}, status=status.HTTP_404_NOT_FOUND)
        
        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteCartById(APIView):
    def delete(self, request, cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
            cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)