from django.contrib import admin
from .models import Product

# Registering model.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'price', 'description', 'image', 'date']
