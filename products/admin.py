from django.contrib import admin

from .models import Category, Product, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'image']
    search_fields = ['title', 'slug']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'slug', 'image']
    search_fields = ['title', 'slug']
    list_filter = ['category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'subcategory', 'title', 'slug', '_image', 'preview_image', 'price'
    ]
    search_fields = ['title', 'slug']
