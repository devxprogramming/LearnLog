# Django imports
from django.shortcuts import render
from django.contrib.auth import get_user_model, get_user, login, logout, authenticate
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# DB models import
from .models import LearnLog

# Serializers
from .serializer import LearnLogSerializer

# REST framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class CreateLog(ModelViewSet):
    queryset = LearnLog.objects.all()
    serializer_class = LearnLogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)