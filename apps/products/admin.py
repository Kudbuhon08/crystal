from django.contrib import admin
from apps.products.models import Product, ProductImage

class ProductInline(admin.TabularInline):
    model = ProductImage  # Assuming ProductImage is the model representing product images
    extra = 1  # Adjust the number of extra photo fields as needed

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(Product, ProductAdmin)