from django.shortcuts import render
from rest_framework import generics, mixins
# Create your views here.
from api.models import User
from api.serializers import UserSerializer


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def LoginUser(request, format=None):
    if request.method== 'POST':
        user = User.objects.get()