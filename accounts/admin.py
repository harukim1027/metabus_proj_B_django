from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('userID', 'password', 'email', 'phone_number')
        }),
        ('Personal info', {
            'fields': ('nickname', 'name', 'region', 'password_quiz', 'password_quiz_answer')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    ordering = ("userID",)

    # nickname: CHAR(20) NOT NULL
    # name: CHAR(30) NOT NULL
    # password: CHAR(20) NOT NULL
    # phone_number: CHAR(16) NOT NULL
    # email: CHAR(50) NOT NULL
    # region: CHAR(20) NOT NULL
    # password_quiz: CHAR(30) NOT NULL
    # password_quiz_answer: CHAR(30) NOT NULL
    # created_at: DATETIME NOT NULL
    # updated_at: DATETIME NOT NULL

    #
    list_display = ['userID', 'nickname', 'is_active']
    list_display_links = ['userID']

