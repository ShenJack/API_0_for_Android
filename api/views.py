from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, mixins, status
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User
from api.serializers import UserSerializer


@api_view(['GET', 'POST'])
def CreateUser(request, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ListUser(request, format=None):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def LoginUser(request, format=None):
    # if request.method== 'POST':
    body = request.POST
    user = User.objects.filter(name=body['name'])[0]
    attempt = body['password']
    password = user.password
    if password==attempt:
        return HttpResponse('Success')
    else:
        return HttpResponse('Failed')
