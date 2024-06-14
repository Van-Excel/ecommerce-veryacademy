from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .basket import Basket
from store.models import Products

# Create your views here.


def basket(request):

    return render(request, 'basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id =int(request.POST.get('productid'))
        product = get_object_or_404(Products, id = product_id)
        basket.add(product= product)
        response = JsonResponse({'test':'data'})
        return response

    