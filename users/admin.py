from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "RGPD",
            {"fields": ("age", "can_be_contacted", "can_data_be_shared")},
        ),
    )
    list_display = UserAdmin.list_display + (
        "age",
        "can_be_contacted",
        "can_data_be_shared",
    )
