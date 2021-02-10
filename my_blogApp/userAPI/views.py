from django.shortcuts import render
from .serializers import UserSerializer
from .models import Account
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class UserDetailAPI(GenericAPIView):
    def post(self, request):
        data = request.data
        token = data['token']
        obj = Token.objects.get(key=token)

        user = obj.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateAPI(GenericAPIView):
    def post(self, request):
        data = request.data
        
        if ('username' in data) or ('password' in data):
            return Response({'detail': 'Username or Password can\'t be change.'}, status=status.HTTP_400_BAD_REQUEST)

        token = Token.objects.get(key=data['token'])
        user = token.user
        
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.mobile_no = data.get('mobile_no', user.mobile_no)
        user.date_of_birth = data.get('date_of_birth', user.date_of_birth)
        user.image = data.get('image', user.image)

        user.save()        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


