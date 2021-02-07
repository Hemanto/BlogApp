from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Account


class AccountAdmin(BaseUserAdmin):
    list_display = ('username','first_name', 'last_name', 'email', 'date_of_birth', 'is_staff',  'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'is_active','is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','email', 'date_of_birth', 'image', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'is_active','is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','email', 'date_of_birth', 'image', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    ordering = ('username',)

admin.site.register(Account, AccountAdmin)









# from django.contrib import admin
# from .models import UserProfile


# admin.site.register(UserProfile)
