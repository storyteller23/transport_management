from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Transport management',
            {
                'fields': (
                'fullname',
                'gender',
                'birth_date',
                'role',
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Transport management',
            {
                'fields': (
                'fullname',
                'gender',
                'birth_date',
                'role',
                )
            }
        )
    )

    list_display = ['username', 'fullname', 'gender', 'birth_date', 'role']
