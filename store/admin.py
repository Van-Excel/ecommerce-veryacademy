from django.contrib import admin

from .models import Category, Products

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    
    
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated' ]
    
    
    list_filter = ['in_stock', 'is_active']
    prepopulated_fields = {'slug':('title',)}
    

