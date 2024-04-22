# wallets/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wallet, User
from .serializers import WalletSerializer
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render


class WalletCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            # Extract user data from the request
            user_data = serializer.validated_data.pop('user')
            
            # Create or retrieve the user
            user, created = User.objects.get_or_create(**user_data)
            
            # Create a new wallet for the user
            wallet = Wallet.objects.create(user=user, **serializer.validated_data)
            
            # Serialize the created wallet and return the response
            return Response(WalletSerializer(wallet).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

def read_password_file():
    try:
        with open('password.txt', 'r') as file:
            lines = file.readlines()
            credentials = {}
            for line in lines:
                username, password = line.strip().split(',')
                credentials[username] = password
            return credentials
    except FileNotFoundError:
        print("Password file not found.")
        return {}

def authenticate_user(username, password):
    credentials = read_password_file()
    if username in credentials and credentials[username] == password:
        return True
    else:
        return False

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if authenticate_user(username, password):
            # Redirect user to home page if credentials are correct
            return redirect('home')
        else:
            # Display error message if credentials are incorrect
            return HttpResponse("Invalid username or password")
    else:
        # Render login form if request method is GET
        return render(request, 'home.html')
