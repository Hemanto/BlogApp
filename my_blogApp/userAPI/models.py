from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from userAPI.managers import AccountManager
from django.utils import timezone


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    mobile_no = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='user/cover_image/', blank=True, null=True)
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'date_of_birth']

    def get_full_name(self):
        return self.first_name + self.last_name

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'



# Custom model

# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=10)
#     date_of_birth = models.DateField()
#     about = models.TextField(null=True, blank=True)
#     image = models.ImageField(upload_to='user/profile_image/', blank=True, null=True)

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name

    