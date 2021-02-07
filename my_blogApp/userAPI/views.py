# from django.shortcuts import render
# from .serializers import UserProfileSerializer, UserSerializer
# from rest_framework import viewsets, status
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response


# class UserCreateView(GenericAPIView):
#     def post(self, request):
#         data = request.data
#         user_data = {
#             'username': data['username'],
#             'password': data['password']
#         }
#         user_serializer = UserSerializer(data=user_data)
#         user_serializer.is_valid(raise_exception=True)
#         user = user_serializer.save()

#         profile_data = {
#             'user': user.id,
#             'first_name': data['first_name'],
#             'last_name': data['last_name'],
#             'email': data['email'],
#             'date_of_birth': data['date_of_birth'],
#             'about': data['about'],
#             'mobile': data['mobile']
#         }
#         profile_serializer = UserProfileSerializer(data=profile_data)
#         profile_serializer.is_valid(raise_exception=True)
#         profile_serializer.save()

#         return Response({'user': user_serializer.data, 'profile': profile_serializer.data})



