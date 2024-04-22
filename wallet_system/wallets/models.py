# wallets/models.py
from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        app_label = 'wallets'

class Wallet(models.Model):
    WALLET_TYPES = [
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('business', 'Business'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_type = models.CharField(max_length=20, choices=WALLET_TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    minimum_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.user}'s {self.wallet_type} Wallet"

    class Meta:
        app_label = 'wallets'
