# wallet_system/urls.py

from django.urls import path
from wallets import views  # Import the views module from the wallets app

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),  # Add the login URL pattern
    # Other URL patterns...
]
