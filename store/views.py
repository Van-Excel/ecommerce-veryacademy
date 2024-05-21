from django.shortcuts import render
from .models import Category, Products


# Create your views here.


def all_products(request):
    
    #It is an SQL query. SELECT * from Products table
    productList = Products.objects.all()
    
    return render(request,  'store/home.html', {'product': productList})
