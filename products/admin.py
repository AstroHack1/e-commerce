import red
from django.contrib import admin

from .models import ProductCategory, Product

# Register your models here.

@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ('name', 'description')


# в админке на гловном странице продуктов добавим поля list_display
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # поля для отображения на главном странице админки products
    list_display = ('name', 'price', 'quantity', 'category')
    # поиск продуктов в нашем случай это по name
    search_fields = ('name',)
    # сортировка по альфавитном порядке
    ordering = ('name',)


