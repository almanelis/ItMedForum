from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Skill, User

"""Вывод информации о пользователе в админке"""
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (_('Extra Fields'), {'fields': ('username', 'password')}),
        (_('Персональная информация'), {'fields': ('first_name', 'last_name', 'middle_name', 'email')}),
        (_('Разрешения'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        (_('Умения'), {
            'fields': ('skill',),
        }),
        (_('Важные даты'), {'fields': ('last_login', 'date_joined')}),
        (_('Дополнительная информация'), {'fields': ('phone', 'avatar')}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Skill)