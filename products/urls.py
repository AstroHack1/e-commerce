from django.urls import path

from .views import IndexView, ProductsListView, basket_add, basket_remove, Product_add


app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products_add/', Product_add, name='blog'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('category/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
