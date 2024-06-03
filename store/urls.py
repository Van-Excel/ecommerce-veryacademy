from django.urls import path
from . import views

app_name = 'store'


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('store/product/<slug:slug>', views.product_details, name="product_detail"),
    path('search/<slug:category_slug>', views.categories_list, name="categories")
]
