# wallets/urls.py

from django.urls import path
from .views import WalletCreateAPIView, WalletDetailAPIView
from . import views


urlpatterns = [
    path('create/', WalletCreateAPIView.as_view(), name='wallet-create'),
    path('detail/<int:user_id>/', WalletDetailAPIView.as_view(), name='wallet-detail'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),  # Add this line for login functionality
]