from django.contrib import admin

from .models import Post

admin.site.empty_value_display = 'Не задано'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at',)
    filter_horizontal = ('tags',)


"""Вывод информации о посте в админке"""
admin.site.register(Post, PostAdmin)
