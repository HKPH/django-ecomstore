from rest_framework import serializers
from .models import User, FullName, Account, Address

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'country']

class UserSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer()
    account = AccountSerializer()
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ['id', 'birthday', 'email', 'phone_number', 'full_name', 'account', 'address']

    def create(self, validated_data):
        full_name_data = validated_data.pop('full_name')
        account_data = validated_data.pop('account')
        address_data = validated_data.pop('address')

        full_name = FullName.objects.create(**full_name_data)
        account = Account.objects.create(**account_data)
        address = Address.objects.create(**address_data)

        user = User.objects.create(full_name=full_name, account=account, address=address, **validated_data)
        return user


class UserEditSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer(required=False)
    account = AccountSerializer(required=False)
    address = AddressSerializer(required=False)

    class Meta:
        model = User
        fields = ['birthday', 'email', 'phone_number', 'full_name', 'account', 'address']

    def update(self, instance, validated_data):
        full_name_data = validated_data.pop('full_name', None)
        account_data = validated_data.pop('account', None)
        address_data = validated_data.pop('address', None)

        if full_name_data:
            FullName.objects.filter(pk=instance.full_name.id).update(**full_name_data)
        if account_data:
            Account.objects.filter(pk=instance.account.id).update(**account_data)
        if address_data:
            Address.objects.filter(pk=instance.address.id).update(**address_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
