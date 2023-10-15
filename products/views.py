from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import ProductCategory, Product, Basket
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from Mixin.views import TitleMixin
# Create your views here.


class IndexView(TitleMixin, TemplateView):
    template_name = 'index.html'
    title = 'Store'

def Product_add(request):
    return render(request=request, template_name='blog.html')

class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products.html'
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context

# функция корзинки добавления
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    context = {
        'products': Product.objects.all(),
        'basket': Basket.objects.all(),
    }
    # проверяем на наличии есть ли продукт
    if not baskets.exists():
        # если нет создадим в продукт
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        # если есть то добавим в корзинку
        basket = baskets.first()
        # количество 1
        basket.quantity += 1
        # сохраняем
        basket.save()
    # перекидоваем пользователя на тот же страницу где он находится
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# уадаления продуктов из корзинки
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
