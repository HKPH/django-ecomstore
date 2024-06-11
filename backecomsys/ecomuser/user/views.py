from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User, Account, FullName, Address
from .serializers import UserSerializer, UserEditSerializer
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

class UserRegistration(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        account = Account.objects.create(username=username, password=password)
        
        try:
            user = User.objects.create(account=account, email=email)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'An error occurred while creating the user'}, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(request.data)
        try:
            account = Account.objects.get(username=username)
        except Account.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if account.password == password:
            user = get_object_or_404(User, account=account)
            return Response({'id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfile(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        data = request.data
        address = get_object_or_404(Address, id=user.address_id)
        full_name = get_object_or_404(FullName, id=user.full_name_id)
        account = get_object_or_404(Account, id=user.account_id)
        print(data)
    
        user.email = data.get('email', user.email)
        user.birthday = data.get('birthday', user.birthday)
        user.phone_number = data.get('phone_number', user.phone_number)


        full_name_data = data.get('full_name', {})
        full_name.first_name = full_name_data.get('first_name', full_name.first_name)
        full_name.last_name = full_name_data.get('last_name', full_name.last_name)

        address_data = data.get('address', {})
        address.street = address_data.get('street', address.street)
        address.city = address_data.get('city', address.city)
        address.state = address_data.get('state', address.state)
        address.country = address_data.get('country', address.country)
        print(address_data)
        account_data=data.get('account',{})
        account.username=account_data.get('username',account.username)
        account.password=account_data.get('password',account.password)
        user.save()
        account.save()
        address.save()
        full_name.save()

        return Response({'message': 'User update successfully'}, status=status.HTTP_201_CREATED)