# Django imports

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model

# REST framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ViewSet

# Serializers
from .serializer import CustomUserSerializer

# Forms
from .forms import RegisterForm

User = get_user_model()



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get("password")

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=username).first()

        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_404_NOT_FOUND)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
    
class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    