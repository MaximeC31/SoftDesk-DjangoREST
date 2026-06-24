from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (  # type: ignore[assignment, operator]
        (
            "RGPD",
            {"fields": ("age", "can_be_contacted", "can_data_be_shared")},
        ),
    )

    list_display = UserAdmin.list_display + (  # type: ignore[operator]
        "age",
        "can_be_contacted",
        "can_data_be_shared",
    )


admin.site.register(User, CustomUserAdmin)
