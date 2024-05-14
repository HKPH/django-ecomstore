from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User  
from rest_framework.authtoken.models import Token  
from .serializers import UserSerializer, UserEditSerializer 
from django.contrib.auth import login
from rest_framework.authtoken.models import Token  
class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Tìm kiếm người dùng trong cơ sở dữ liệu bằng tên người dùng (username)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Kiểm tra mật khẩu
        if user.password == password:
            # Đăng nhập thành công, trả về id của người dùng
            return Response({'id': user.id}, status=status.HTTP_200_OK)
        else:
            # Sai tên đăng nhập hoặc mật khẩu
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfile(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserEditSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
