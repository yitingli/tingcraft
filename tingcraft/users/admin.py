from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name',)
    search_fields = ['username', 'email']
    date_hierarchy = 'date_joined'

admin.site.register(User, UserAdmin)
