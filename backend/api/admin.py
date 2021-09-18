from django.contrib import admin

from .models import Category, Product


admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Author', 'Slug', 'Price',]
    list_editable = ['Price']
    prepopulated_fields = {'slug': ('title',)}