from django.contrib import admin
from .models import Company, Category

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}
#     list_display = ['name', 'quantity', 'price', 'discount', 'category']
#     list_editable = ['discount']
#     search_fields = ['name', 'description']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = [
        'name',
        'slug',
        'address',
        'contact_info',
        'unique_code',
        'image',
        'category',
        'created_at',
    ]
    search_fields = ['name', 'slug', 'unique_code', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']




