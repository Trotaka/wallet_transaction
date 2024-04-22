from rest_framework import serializers
from .models import User, Wallet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']

class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Wallet
        fields = ['user', 'wallet_type', 'balance', 'minimum_balance']
