from django.contrib import admin
from .models import Client, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'company']
    search_fields = ['user', 'company']




