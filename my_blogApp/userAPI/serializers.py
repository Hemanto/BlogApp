from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'password', 'email',
                  'mobile_no', 'image', 'date_of_birth']

        # password will not be render with the user
        extra_kwargs = {'password': {'write_only': True}}

    # override create method for password hashing
    def create(self, validated_data):
        user = Account(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            mobile_no=validated_data['mobile_no'],
            username=validated_data['username'],
            date_of_birth=validated_data['date_of_birth']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username',
                  'password', 'email', 'date_of_birth']

    def save(self, request):
        user = Account(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            # mobile_no = request.data['mobile_no'],
            username=request.data['username'],
            date_of_birth=request.data['date_of_birth'],
            # image = request.data['image'],
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
        user.set_password(request.data['password'])
        user.save()
        return user


# from rest_framework import serializers
# from .models import UserProfile
# from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

#         # password will not be render with the user
#         extra_kwargs = {'password': {'write_only': True}}

#     # override create method for password hashing
#     def create(self, validated_data):
#         user = User(
#             username=validated_data['username']
#         )

#         user.set_password(validated_data['password'])
#         user.save()
#         return user


# class UserProfileSerializer(serializers.ModelSerializer):
#     # user = UserSerializer()
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

# class MainUserSerializer(serializers.Serializer):
#     user = UserSerializer()
#     profile = UserProfileSerializer()