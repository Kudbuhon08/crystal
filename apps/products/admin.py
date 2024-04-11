from django.contrib import admin
from .models import Product, ProductImage, ProductCard

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductCardInline(admin.TabularInline):
    model = ProductCard
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductCardInline]

admin.site.register(Product, ProductAdmin)
