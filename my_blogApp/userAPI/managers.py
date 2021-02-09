from django.db import models
from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name, 
            last_name = last_name,
            email = email,
            username=username,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, email, username, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name, 
            last_name = last_name,
            email = email,
            username=username,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
