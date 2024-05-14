
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'birthday', 'email', 'phone_number', 'address']

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'birthday', 'email', 'phone_number', 'address']
