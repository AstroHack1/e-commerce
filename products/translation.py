from modeltranslation.translator import register, TranslationOptions
from .models import Basket, ProductCategory, Product


@register(Basket)
class BasketTranslationOption(TranslationOptions):
    fields = ('product', 'quantity')

@register(ProductCategory)
class BasketTranslationOption(TranslationOptions):
    fields = ('name', 'description')

@register(Product)
class BasketTranslationOption(TranslationOptions):
    fields = ('name', 'description')

