from django.contrib import admin
from .models.product import product
from .models.category import category


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(product, AdminProduct)
admin.site.register(category, AdminCategory)
